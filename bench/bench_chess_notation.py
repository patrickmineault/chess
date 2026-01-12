#!/usr/bin/env python3
"""
Benchmark models on generating mate-in-1 chess scenarios in FEN notation.

This script asks models to describe mate-in-1 scenarios with:
- A creative name for the scenario
- FEN notation for the board position
- The winning move for white

Usage:
    python bench_chess_notation.py --num 3 --models anthropic/claude-sonnet-4.5
    python bench_chess_notation.py --num 5 --all-models
    python bench_chess_notation.py --list-models
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

PROMPT_TEMPLATE = """Describe {num} mate-in-1 scenarios for white. Put each scenario in its own code fences (three backticks); for each scenario, the first line should be the name of the scenario, the second line the FEN notation for the setup, the third line the winning move for white. The scenarios should be valid and distinct from each other."""

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


def parse_scenarios(content: str) -> list[dict]:
    """
    Parse mate-in-1 scenarios from model response.

    Expected format in code fences:
    ```
    Scenario Name
    FEN notation
    Winning move
    ```

    Returns list of dicts with keys: name, fen, move
    """
    scenarios = []

    # Find all code blocks
    code_block_pattern = r"```(?:\w*\n)?([\s\S]*?)```"
    matches = re.findall(code_block_pattern, content)

    for match in matches:
        lines = [line.strip() for line in match.strip().split("\n") if line.strip()]

        if len(lines) >= 3:
            scenario = {
                "name": lines[0],
                "fen": lines[1],
                "move": lines[2],
            }
            scenarios.append(scenario)
        elif len(lines) == 2:
            # Sometimes move might be missing or combined
            scenario = {
                "name": lines[0],
                "fen": lines[1],
                "move": "",
            }
            scenarios.append(scenario)

    return scenarios


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
    scenarios: list[dict],
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

    # Save parsed scenarios as JSON
    (result_dir / "scenarios.json").write_text(json.dumps(scenarios, indent=2))

    # Save metadata
    metadata = {
        "model": model_name,
        "effort": effort,
        "num_scenarios_requested": num,
        "num_scenarios_parsed": len(scenarios),
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

        scenarios = parse_scenarios(result["content"])

        run_number = save_results(
            output_dir=output_dir,
            model_name=model_name,
            effort=effort,
            num=num,
            content=result["content"],
            reasoning=result["reasoning"],
            scenarios=scenarios,
            usage=result["usage"],
            raw_response=result["raw_response"],
        )

        return {
            "model": model_name,
            "effort": effort,
            "num_requested": num,
            "num_parsed": len(scenarios),
            "run": run_number,
            "success": len(scenarios) >= num,
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
            "num_parsed": 0,
            "run": None,
            "success": False,
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
                status = (
                    "OK"
                    if result["success"]
                    else f"PARTIAL ({result['num_parsed']}/{result['num_requested']})"
                )
                reasoning = "with reasoning" if result["has_reasoning"] else ""
                print(
                    f"    {status} (run_{result['run']}, {result['elapsed_seconds']:.1f}s) {reasoning}"
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
                    status = (
                        "OK"
                        if result["success"]
                        else f"PARTIAL ({result['num_parsed']}/{result['num_requested']})"
                    )
                    reasoning = "with reasoning" if result["has_reasoning"] else ""
                    print(
                        f"[{completed}/{len(tasks)}] {task['model_name']} | effort={task['effort']} | num={task['num']}"
                    )
                    print(
                        f"    {status} (run_{result['run']}, {result['elapsed_seconds']:.1f}s) {reasoning}"
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


def print_summary(results: list[dict]):
    """Print a formatted summary table."""
    print("\n" + "=" * 100)
    print("BENCHMARK SUMMARY - Chess Notation (FEN) Generation")
    print("=" * 100)
    print(
        f"{'Model':<35} {'Effort':<8} {'Req':<5} {'Got':<5} {'Run':<5} {'OK':<6} {'Reasoning':<10} {'Time':<8}"
    )
    print("-" * 100)

    for r in results:
        ok_status = "Yes" if r.get("success") else "No"
        reasoning_status = "Yes" if r.get("has_reasoning") else "No"
        time_str = (
            f"{r.get('elapsed_seconds', 0):.1f}s" if "elapsed_seconds" in r else "N/A"
        )
        run_str = str(r.get("run", "N/A"))
        model_short = r["model"][:34] if len(r["model"]) > 34 else r["model"]
        print(
            f"{model_short:<35} {r.get('effort', 'N/A'):<8} {r['num_requested']:<5} {r['num_parsed']:<5} {run_str:<5} {ok_status:<6} {reasoning_status:<10} {time_str:<8}"
        )

    # Print consistency stats if there are multiple runs
    if len(results) > 1:
        print("\n" + "-" * 100)
        print("CONSISTENCY STATS")
        print("-" * 100)

        # Group by model/effort/num
        from collections import defaultdict

        groups = defaultdict(list)
        for r in results:
            key = (r["model"], r.get("effort", "N/A"), r["num_requested"])
            groups[key].append(r.get("success", False))

        for (model, effort, num), successes in sorted(groups.items()):
            if len(successes) > 1:
                success_rate = sum(successes) / len(successes) * 100
                model_short = model[:34] if len(model) > 34 else model
                print(
                    f"{model_short:<35} {effort:<8} {num:<5} {success_rate:>5.0f}% success ({sum(successes)}/{len(successes)} runs)"
                )

    print("=" * 100)


def main():
    parser = argparse.ArgumentParser(
        description="Benchmark models on generating mate-in-1 chess scenarios in FEN notation",
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
        help="Number of scenarios to request (can specify multiple)",
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
        default="./results_cn",
        help="Output directory for results (default: ./results_cn)",
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
    output_dir = Path(args.output)

    total_combinations = len(models) * len(args.num) * len(efforts) * args.runs
    print(
        f"Benchmarking {len(models)} models × {len(efforts)} efforts × {len(args.num)} nums × {args.runs} runs = {total_combinations} total"
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
