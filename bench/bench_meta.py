#!/usr/bin/env python3
"""
Meta-benchmark: Ask models to predict their own performance on chess mate-in-1 generation.

This script asks models how well they think they would do on the mate-in-1 task,
requesting a probability estimate and explanation.

Usage:
    python bench_meta.py --num 3 --models anthropic/claude-sonnet-4.5
    python bench_meta.py --num 5 --all-models
    python bench_meta.py --list-models
"""

import argparse
import json
import os
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path

import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# OpenRouter API endpoint
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

# Models to benchmark (OpenRouter model IDs)
AVAILABLE_MODELS = {
    "anthropic/claude-sonnet-4.5",
    "anthropic/claude-opus-4.5",
    "openai/gpt-5.1",
    "google/gemini-3-pro-preview",
    "moonshotai/kimi-k2-thinking",
    "qwen/qwen3-vl-235b-a22b-instruct",
}

PROMPT_TEMPLATE = """If I was to ask you a question like this, how well do you think you think you would be able to succesfully complete the task? Write your answer as a json string, {{"p": float, "explanation": str}}

Describe {num} mate-in-1 scenarios for white. Put each scenario in its own code fences (three backticks); for each scenario, the first line should be the name of the scenario, the second line the FEN notation for the setup, the third line the winning move for white. The scenarios should be valid and distinct from each other."""

# Reasoning effort levels
EFFORT_LEVELS = ["none", "low", "medium", "high"]


def get_api_key():
    """Get OpenRouter API key from environment or .env file."""
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        raise ValueError(
            "OPENROUTER_API_KEY not found. "
            "Create a .env file with OPENROUTER_API_KEY=your-key "
            "or get a key at https://openrouter.ai/keys"
        )
    return api_key


def call_openrouter(
    model_id: str, prompt: str, api_key: str, effort: str = "none"
) -> dict:
    """
    Call OpenRouter API and return full response.

    Args:
        model_id: OpenRouter model identifier
        prompt: The prompt to send
        api_key: OpenRouter API key
        effort: Reasoning effort level (none, low, medium, high)

    Returns dict with:
        - content: The main response text
        - reasoning: Reasoning trace if available (for thinking models)
        - raw_response: Full API response
        - usage: Token usage stats
    """
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/your-repo",  # Optional
    }

    payload = {
        "model": model_id,
        "messages": [{"role": "user", "content": prompt}],
    }

    # Configure reasoning based on effort level
    if effort != "none":
        payload["reasoning"] = {
            "effort": effort,
        }

    response = requests.post(
        OPENROUTER_API_URL,
        headers=headers,
        json=payload,
        timeout=600,  # 10 min timeout for reasoning models
    )
    response.raise_for_status()

    data = response.json()

    result = {
        "content": "",
        "reasoning": None,
        "raw_response": data,
        "usage": data.get("usage", {}),
    }

    if "choices" in data and len(data["choices"]) > 0:
        message = data["choices"][0].get("message", {})
        result["content"] = message.get("content", "")

        # Extract reasoning if present (different models use different fields)
        if "reasoning" in message:
            result["reasoning"] = message["reasoning"]
        elif "reasoning_content" in message:
            result["reasoning"] = message["reasoning_content"]

    return result


def parse_meta_response(content: str) -> dict:
    """
    Parse the meta prediction response from the model.

    Expected format: JSON with keys "p" (float) and "explanation" (str)

    Returns dict with keys: p, explanation, parse_success
    """
    result = {
        "p": None,
        "explanation": None,
        "parse_success": False,
    }

    # Try to find JSON in the response
    # First, try to find JSON in code blocks
    code_block_pattern = r"```(?:json)?\s*([\s\S]*?)```"
    matches = re.findall(code_block_pattern, content)

    json_str = None
    if matches:
        json_str = matches[0].strip()
    else:
        # Try to find raw JSON object in text
        json_pattern = r'\{[^{}]*"p"\s*:\s*[\d.]+[^{}]*\}'
        json_match = re.search(json_pattern, content)
        if json_match:
            json_str = json_match.group(0)

    if json_str:
        try:
            parsed = json.loads(json_str)
            if "p" in parsed:
                result["p"] = float(parsed["p"])
                result["explanation"] = parsed.get("explanation", "")
                result["parse_success"] = True
        except (json.JSONDecodeError, ValueError, TypeError):
            pass

    return result


def get_next_run_number(base_dir: Path) -> int:
    """Find the next available run number in a directory."""
    if not base_dir.exists():
        return 1

    existing_runs = [
        d for d in base_dir.iterdir() if d.is_dir() and d.name.startswith("run_")
    ]

    if not existing_runs:
        return 1

    run_numbers = []
    for run_dir in existing_runs:
        try:
            run_num = int(run_dir.name.split("_")[1])
            run_numbers.append(run_num)
        except (IndexError, ValueError):
            continue

    return max(run_numbers, default=0) + 1


def save_results(
    output_dir: Path,
    model_name: str,
    effort: str,
    num: int,
    content: str,
    reasoning: str | None,
    parsed: dict,
    usage: dict,
    raw_response: dict,
) -> int:
    """Save all results to organized files. Returns the run number."""
    base_dir = output_dir / model_name / f"effort_{effort}" / f"num_{num}"
    run_number = get_next_run_number(base_dir)
    result_dir = base_dir / f"run_{run_number}"
    result_dir.mkdir(parents=True, exist_ok=True)

    # Save full response
    (result_dir / "response.md").write_text(content)

    # Save reasoning trace if available
    if reasoning:
        (result_dir / "reasoning.md").write_text(reasoning)

    # Save parsed prediction as JSON
    (result_dir / "prediction.json").write_text(json.dumps(parsed, indent=2))

    # Save metadata
    metadata = {
        "model": model_name,
        "effort": effort,
        "num_scenarios_requested": num,
        "predicted_p": parsed.get("p"),
        "parse_success": parsed.get("parse_success", False),
        "run": run_number,
        "timestamp": datetime.now().isoformat(),
        "usage": usage,
        "has_reasoning": reasoning is not None,
    }
    (result_dir / "metadata.json").write_text(json.dumps(metadata, indent=2))

    # Save raw response for debugging
    (result_dir / "raw_response.json").write_text(json.dumps(raw_response, indent=2))

    return run_number


def count_existing_runs(
    output_dir: Path, model_name: str, effort: str, num: int
) -> int:
    """Count how many runs already exist for this combination."""
    base_dir = output_dir / model_name / f"effort_{effort}" / f"num_{num}"
    if not base_dir.exists():
        return 0

    existing_runs = [
        d for d in base_dir.iterdir() if d.is_dir() and d.name.startswith("run_")
    ]
    return len(existing_runs)


def execute_single_run(
    model_name: str,
    prompt: str,
    effort: str,
    num: int,
    output_dir: Path,
    api_key: str,
) -> dict:
    """Execute a single benchmark run. Returns result dict."""
    try:
        start_time = time.time()
        result = call_openrouter(model_name, prompt, api_key, effort)
        elapsed = time.time() - start_time

        parsed = parse_meta_response(result["content"])

        run_number = save_results(
            output_dir=output_dir,
            model_name=model_name,
            effort=effort,
            num=num,
            content=result["content"],
            reasoning=result["reasoning"],
            parsed=parsed,
            usage=result["usage"],
            raw_response=result["raw_response"],
        )

        return {
            "model": model_name,
            "effort": effort,
            "num_requested": num,
            "predicted_p": parsed.get("p"),
            "parse_success": parsed.get("parse_success", False),
            "explanation": parsed.get("explanation"),
            "run": run_number,
            "has_reasoning": result["reasoning"] is not None,
            "elapsed_seconds": elapsed,
            "tokens": result["usage"],
            "error": None,
        }

    except Exception as e:
        return {
            "model": model_name,
            "effort": effort,
            "num_requested": num,
            "predicted_p": None,
            "parse_success": False,
            "explanation": None,
            "run": None,
            "has_reasoning": False,
            "elapsed_seconds": 0,
            "tokens": {},
            "error": str(e),
        }


def run_benchmark(
    models: list[str],
    num_scenarios: list[int],
    effort_levels: list[str],
    num_runs: int,
    output_dir: Path,
    api_key: str,
    max_parallel: int = 1,
):
    """Run benchmark across all model/num/effort combinations."""
    # Build list of tasks to execute
    tasks = []
    skipped = 0

    for model_name in models:
        for effort in effort_levels:
            for num in num_scenarios:
                prompt = PROMPT_TEMPLATE.format(num=num)

                # Check how many runs already exist
                existing_runs = count_existing_runs(output_dir, model_name, effort, num)
                runs_needed = max(0, num_runs - existing_runs)

                if runs_needed == 0:
                    print(
                        f"SKIP: {model_name} | effort={effort} | num={num} (have {existing_runs}/{num_runs})"
                    )
                    skipped += num_runs
                    continue

                for _ in range(runs_needed):
                    tasks.append(
                        {
                            "model_name": model_name,
                            "prompt": prompt,
                            "effort": effort,
                            "num": num,
                        }
                    )

    if not tasks:
        print(f"\nNo new runs needed. Skipped: {skipped}")
        return []

    print(f"\nExecuting {len(tasks)} runs with {max_parallel} parallel workers...")
    print(f"(Skipped {skipped} existing runs)\n")

    results_summary = []

    if max_parallel == 1:
        # Sequential execution
        for i, task in enumerate(tasks):
            print(
                f"[{i+1}/{len(tasks)}] {task['model_name']} | effort={task['effort']} | num={task['num']}"
            )

            result = execute_single_run(
                model_name=task["model_name"],
                prompt=task["prompt"],
                effort=task["effort"],
                num=task["num"],
                output_dir=output_dir,
                api_key=api_key,
            )

            if result["error"]:
                print(f"    ERROR: {result['error']}")
            else:
                p_str = f"p={result['predicted_p']:.2f}" if result["predicted_p"] is not None else "p=N/A"
                parse_status = "parsed" if result["parse_success"] else "PARSE FAILED"
                reasoning = "with reasoning" if result["has_reasoning"] else ""
                print(
                    f"    {p_str} ({parse_status}, run_{result['run']}, {result['elapsed_seconds']:.1f}s) {reasoning}"
                )

            results_summary.append(result)
            time.sleep(0.5)  # Small delay between requests
    else:
        # Parallel execution
        completed = 0
        with ThreadPoolExecutor(max_workers=max_parallel) as executor:
            future_to_task = {
                executor.submit(
                    execute_single_run,
                    model_name=task["model_name"],
                    prompt=task["prompt"],
                    effort=task["effort"],
                    num=task["num"],
                    output_dir=output_dir,
                    api_key=api_key,
                ): task
                for task in tasks
            }

            for future in as_completed(future_to_task):
                task = future_to_task[future]
                completed += 1
                result = future.result()

                if result["error"]:
                    print(
                        f"[{completed}/{len(tasks)}] {task['model_name']} | effort={task['effort']} | num={task['num']}"
                    )
                    print(f"    ERROR: {result['error']}")
                else:
                    p_str = f"p={result['predicted_p']:.2f}" if result["predicted_p"] is not None else "p=N/A"
                    parse_status = "parsed" if result["parse_success"] else "PARSE FAILED"
                    reasoning = "with reasoning" if result["has_reasoning"] else ""
                    print(
                        f"[{completed}/{len(tasks)}] {task['model_name']} | effort={task['effort']} | num={task['num']}"
                    )
                    print(
                        f"    {p_str} ({parse_status}, run_{result['run']}, {result['elapsed_seconds']:.1f}s) {reasoning}"
                    )

                results_summary.append(result)

    # Save summary (append to existing if present)
    summary_path = output_dir / "summary.json"
    if summary_path.exists() and results_summary:
        existing = json.loads(summary_path.read_text())
        existing.extend(results_summary)
        summary_path.write_text(json.dumps(existing, indent=2))
    elif results_summary:
        output_dir.mkdir(parents=True, exist_ok=True)
        summary_path.write_text(json.dumps(results_summary, indent=2))

    executed = len([r for r in results_summary if r["error"] is None])
    errors = len([r for r in results_summary if r["error"] is not None])
    print(f"\nResults saved to {output_dir}")
    print(f"Executed: {executed}, Errors: {errors}, Skipped: {skipped}")

    return results_summary


def recompile_summary(output_dir: Path) -> list[dict]:
    """
    Recompile summary.json from all cached metadata.json files.

    Walks through the output directory structure and rebuilds the summary
    from individual run metadata files.
    """
    results = []

    if not output_dir.exists():
        print(f"Output directory does not exist: {output_dir}")
        return results

    # Walk through directory structure: model/effort_X/num_Y/run_Z/
    for model_dir in output_dir.iterdir():
        if not model_dir.is_dir() or model_dir.name == "summary.json":
            continue

        # Handle nested model names like "anthropic/claude-sonnet-4.5"
        # which become "anthropic/claude-sonnet-4.5" directories
        model_name = model_dir.name

        # Check if this is a provider directory (contains model subdirs)
        subdirs = [d for d in model_dir.iterdir() if d.is_dir()]
        if subdirs and not any(d.name.startswith("effort_") for d in subdirs):
            # This is a provider dir, iterate through model subdirs
            for submodel_dir in subdirs:
                model_name = f"{model_dir.name}/{submodel_dir.name}"
                results.extend(_collect_runs_from_model_dir(submodel_dir, model_name))
        else:
            results.extend(_collect_runs_from_model_dir(model_dir, model_name))

    # Save the recompiled summary
    if results:
        summary_path = output_dir / "summary.json"
        summary_path.write_text(json.dumps(results, indent=2))
        print(f"Recompiled {len(results)} results to {summary_path}")

    return results


def _collect_runs_from_model_dir(model_dir: Path, model_name: str) -> list[dict]:
    """Collect all run results from a model directory."""
    results = []

    for effort_dir in model_dir.iterdir():
        if not effort_dir.is_dir() or not effort_dir.name.startswith("effort_"):
            continue

        effort = effort_dir.name.replace("effort_", "")

        for num_dir in effort_dir.iterdir():
            if not num_dir.is_dir() or not num_dir.name.startswith("num_"):
                continue

            try:
                num_requested = int(num_dir.name.replace("num_", ""))
            except ValueError:
                continue

            for run_dir in num_dir.iterdir():
                if not run_dir.is_dir() or not run_dir.name.startswith("run_"):
                    continue

                metadata_path = run_dir / "metadata.json"
                prediction_path = run_dir / "prediction.json"

                if not metadata_path.exists():
                    continue

                try:
                    metadata = json.loads(metadata_path.read_text())

                    # Load prediction if available
                    prediction = {}
                    if prediction_path.exists():
                        prediction = json.loads(prediction_path.read_text())

                    # Reconstruct result entry
                    result = {
                        "model": model_name,
                        "effort": effort,
                        "num_requested": num_requested,
                        "predicted_p": metadata.get("predicted_p") or prediction.get("p"),
                        "parse_success": metadata.get("parse_success", prediction.get("parse_success", False)),
                        "explanation": prediction.get("explanation"),
                        "run": metadata.get("run"),
                        "has_reasoning": metadata.get("has_reasoning", False),
                        "elapsed_seconds": 0,  # Not stored in metadata
                        "tokens": metadata.get("usage", {}),
                        "error": None,
                    }
                    results.append(result)

                except (json.JSONDecodeError, KeyError) as e:
                    print(f"Warning: Could not parse {metadata_path}: {e}")
                    continue

    return results


def print_summary(results: list[dict]):
    """Print a formatted summary table."""
    print("\n" + "=" * 110)
    print("BENCHMARK SUMMARY - Meta Prediction (Self-Confidence)")
    print("=" * 110)
    print(
        f"{'Model':<35} {'Effort':<8} {'Num':<5} {'Pred P':<8} {'Parsed':<8} {'Run':<5} {'Reasoning':<10} {'Time':<8}"
    )
    print("-" * 110)

    for r in results:
        p_str = f"{r.get('predicted_p'):.2f}" if r.get("predicted_p") is not None else "N/A"
        parse_status = "Yes" if r.get("parse_success") else "No"
        reasoning_status = "Yes" if r.get("has_reasoning") else "No"
        time_str = (
            f"{r.get('elapsed_seconds', 0):.1f}s" if "elapsed_seconds" in r else "N/A"
        )
        run_str = str(r.get("run", "N/A"))
        model_short = r["model"][:34] if len(r["model"]) > 34 else r["model"]
        print(
            f"{model_short:<35} {r.get('effort', 'N/A'):<8} {r['num_requested']:<5} {p_str:<8} {parse_status:<8} {run_str:<5} {reasoning_status:<10} {time_str:<8}"
        )

    # Print average predictions by model if there are multiple runs
    if len(results) > 1:
        print("\n" + "-" * 110)
        print("AVERAGE PREDICTIONS BY MODEL")
        print("-" * 110)

        from collections import defaultdict

        groups = defaultdict(list)
        for r in results:
            if r.get("predicted_p") is not None:
                key = (r["model"], r.get("effort", "N/A"), r["num_requested"])
                groups[key].append(r["predicted_p"])

        for (model, effort, num), predictions in sorted(groups.items()):
            if predictions:
                avg_p = sum(predictions) / len(predictions)
                model_short = model[:34] if len(model) > 34 else model
                print(
                    f"{model_short:<35} {effort:<8} {num:<5} avg_p={avg_p:.2f} ({len(predictions)} runs)"
                )

    print("=" * 110)


def main():
    parser = argparse.ArgumentParser(
        description="Meta-benchmark: Ask models to predict their own performance on chess mate-in-1 generation",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --models anthropic/claude-sonnet-4.5 --num 3
  %(prog)s --models openai/gpt-5.1 --effort high --num 3 5
  %(prog)s --all-models --runs 3 --parallel 4
  %(prog)s --list-models
        """,
    )
    parser.add_argument(
        "--num",
        type=int,
        nargs="+",
        default=[3],
        help="Number of scenarios to ask about (can specify multiple)",
    )
    parser.add_argument(
        "--runs",
        type=int,
        default=1,
        help="Number of times to run each model/num combination (default: 1)",
    )
    parser.add_argument(
        "--parallel",
        type=int,
        default=1,
        help="Number of parallel requests (default: 1, sequential)",
    )
    parser.add_argument(
        "--effort",
        type=str,
        nargs="+",
        choices=EFFORT_LEVELS,
        default=["none"],
        help="Reasoning effort level(s): none, low, medium, high (default: none)",
    )
    parser.add_argument(
        "--all-efforts",
        action="store_true",
        help="Test all effort levels (none, low, medium, high)",
    )
    parser.add_argument(
        "--models",
        nargs="+",
        help="Models to test (use --list-models to see options)",
    )
    parser.add_argument(
        "--all-models",
        action="store_true",
        help="Test all available models",
    )
    parser.add_argument(
        "--list-models",
        action="store_true",
        help="List available models and exit",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="./results_meta",
        help="Output directory for results (default: ./results_meta)",
    )
    parser.add_argument(
        "--recompile",
        action="store_true",
        help="Recompile summary.json from cached results without running any new requests",
    )

    args = parser.parse_args()

    # Show help if no arguments provided
    if len(sys.argv) == 1:
        parser.print_help()
        return

    if args.list_models:
        print("Available models:")
        for model_id in sorted(AVAILABLE_MODELS):
            print(f"  {model_id}")
        return

    output_dir = Path(args.output)

    if args.recompile:
        print(f"Recompiling summary from cached results in {output_dir}...")
        results = recompile_summary(output_dir)
        print_summary(results)
        return

    # Determine which models to run
    if args.all_models:
        models = list(AVAILABLE_MODELS)
    elif args.models:
        models = args.models
    else:
        # Default to a reasonable subset
        models = ["anthropic/claude-sonnet-4.5"]

    # Validate models
    for model in models:
        if model not in AVAILABLE_MODELS:
            print(f"Warning: '{model}' not in predefined models, using as raw model ID")

    # Determine which effort levels to use
    if args.all_efforts:
        efforts = EFFORT_LEVELS
    else:
        efforts = args.effort

    api_key = get_api_key()

    total_combinations = len(models) * len(args.num) * len(efforts) * args.runs
    print(
        f"Meta-benchmarking {len(models)} models × {len(efforts)} efforts × {len(args.num)} nums × {args.runs} runs = {total_combinations} total"
    )
    print(f"Output directory: {output_dir}")

    results = run_benchmark(
        models=models,
        num_scenarios=args.num,
        effort_levels=efforts,
        num_runs=args.runs,
        output_dir=output_dir,
        api_key=api_key,
        max_parallel=args.parallel,
    )

    print_summary(results)


if __name__ == "__main__":
    main()
