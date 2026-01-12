#!/usr/bin/env python3
"""
Aggregate results from iterative chess notation benchmark (bench_chess_notation_iterative.py).

Walks through all results in results_cni/, validates final scenarios for uniqueness,
and creates a results.csv summary.

Usage:
    python aggregate_cni.py
    python aggregate_cni.py --input ./results_cni
"""

import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path

import chess


# ============================================================================
# Board transformation functions for detecting duplicate positions
# ============================================================================


def transform_board(board: chess.Board, transform_func) -> chess.Board:
    """Apply a square transformation to create a new board."""
    new_board = chess.Board(None)  # Empty board
    new_board.turn = board.turn

    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            new_square = transform_func(square)
            new_board.set_piece_at(new_square, piece)

    return new_board


def vertical_flip(square: int) -> int:
    """Flip vertically (rank mirror)."""
    return chess.square_mirror(square)


def horizontal_flip(square: int) -> int:
    """Flip horizontally (file mirror)."""
    file = chess.square_file(square)
    rank = chess.square_rank(square)
    return chess.square(7 - file, rank)


def rotate_180(square: int) -> int:
    """Rotate 180 degrees."""
    file = chess.square_file(square)
    rank = chess.square_rank(square)
    return chess.square(7 - file, 7 - rank)


def get_canonical_board_fen(board: chess.Board) -> str:
    """
    Get canonical representation of a board position.

    Generates all transformations (identity, vertical flip, horizontal flip,
    180 degree rotation) and returns the lexicographically smallest board FEN.
    This allows detecting positions that are equivalent via rotation/reflection.
    """
    transforms = [
        lambda s: s,  # identity
        vertical_flip,
        horizontal_flip,
        rotate_180,
    ]

    fens = []
    for transform in transforms:
        transformed = transform_board(board, transform)
        # Only compare position part of FEN (first field)
        position_fen = transformed.board_fen()
        fens.append(position_fen)

    return min(fens)


# ============================================================================
# Validation functions
# ============================================================================


def validate_fen(fen: str) -> tuple[chess.Board | None, str]:
    """
    Validate FEN notation and return board if valid.

    Returns (board, error_message). Board is None if invalid.
    """
    try:
        board = chess.Board(fen)
    except ValueError as e:
        return None, f"Invalid FEN: {e}"

    if not board.is_valid():
        return None, "Invalid position (illegal board state)"

    return board, ""


def get_canonical_fen_for_scenario(scenario: dict) -> str:
    """Get canonical FEN for a scenario, or empty string if invalid."""
    fen = scenario.get("fen", "")
    board, _ = validate_fen(fen)
    if board is None:
        return ""
    return get_canonical_board_fen(board)


# ============================================================================
# File operations
# ============================================================================


def find_all_runs(input_dir: Path) -> list[Path]:
    """Find all run directories in the results folder."""
    runs = []

    # Pattern: results_cni/{provider}/{model}/effort_{level}/num_{n}/run_{i}
    for run_dir in input_dir.rglob("run_*"):
        if run_dir.is_dir() and (run_dir / "metadata.json").exists():
            runs.append(run_dir)

    return sorted(runs)


def parse_run_path(run_dir: Path, base_dir: Path) -> dict:
    """Extract model, effort, num, run from path."""
    try:
        rel_path = run_dir.relative_to(base_dir)
        parts = rel_path.parts

        # Expected: {provider}/{model}/effort_{level}/num_{n}/run_{i}
        # e.g., anthropic/claude-sonnet-4.5/effort_high/num_3/run_1
        # Model name includes provider: "anthropic/claude-sonnet-4.5"
        if len(parts) >= 5:
            model = f"{parts[0]}/{parts[1]}"
            effort = parts[2].replace("effort_", "")
            num = parts[3].replace("num_", "")
            run = parts[4].replace("run_", "")
        else:
            # Fallback for unexpected structure
            model = "/".join(parts[:-3]) if len(parts) > 3 else ""
            effort = parts[-3].replace("effort_", "") if len(parts) > 2 else ""
            num = parts[-2].replace("num_", "") if len(parts) > 1 else ""
            run = parts[-1].replace("run_", "") if len(parts) > 0 else ""

        return {
            "model": model,
            "effort": effort,
            "num_requested": num,
            "run": run,
        }
    except Exception:
        return {
            "model": "",
            "effort": "",
            "num_requested": "",
            "run": "",
        }


def process_run_folder(run_dir: Path) -> dict | None:
    """
    Process a single run folder and return aggregated results.

    Returns dict with run-level results, or None if invalid.
    """
    metadata_file = run_dir / "metadata.json"
    scenarios_file = run_dir / "scenarios.json"
    validation_file = run_dir / "validation.json"

    if not metadata_file.exists():
        return None

    try:
        metadata = json.loads(metadata_file.read_text())
    except json.JSONDecodeError:
        return None

    # Load scenarios and validation
    scenarios = []
    validations = []

    if scenarios_file.exists():
        try:
            scenarios = json.loads(scenarios_file.read_text())
        except json.JSONDecodeError:
            pass

    if validation_file.exists():
        try:
            validations = json.loads(validation_file.read_text())
        except json.JSONDecodeError:
            pass

    # Calculate canonical FENs for valid scenarios
    canonical_fens = []
    for i, scenario in enumerate(scenarios):
        # Check if this scenario is valid (is_checkmate)
        is_valid = False
        if i < len(validations):
            is_valid = validations[i].get("is_checkmate", False)

        if is_valid:
            canonical = get_canonical_fen_for_scenario(scenario)
            if canonical:
                canonical_fens.append(canonical)

    # Count unique valid scenarios
    unique_canonical_fens = set(canonical_fens)
    num_unique_valid = len(unique_canonical_fens)

    # Build result
    result = {
        "model": metadata.get("model", ""),
        "effort": metadata.get("effort", ""),
        "num_requested": metadata.get("num_scenarios_requested", 0),
        "num_valid": metadata.get("num_scenarios_valid", 0),
        "num_unique_valid": num_unique_valid,
        "num_iterations": metadata.get("num_iterations", 0),
        "perfect": metadata.get("perfect", False),
        "completion_tokens": metadata.get("usage", {}).get("completion_tokens", 0),
        "prompt_tokens": metadata.get("usage", {}).get("prompt_tokens", 0),
        "total_tokens": metadata.get("usage", {}).get("total_tokens", 0),
        "run_dir": str(run_dir),
        "canonical_fens": list(unique_canonical_fens),
    }

    return result


def main():
    parser = argparse.ArgumentParser(
        description="Aggregate iterative chess notation benchmark results",
    )
    parser.add_argument(
        "--input",
        type=str,
        default="./results_cni",
        help="Input directory containing results (default: ./results_cni)",
    )

    args = parser.parse_args()
    input_dir = Path(args.input)

    if not input_dir.exists():
        print(f"Error: Input directory '{input_dir}' does not exist")
        return 1

    # Find all run directories
    run_dirs = find_all_runs(input_dir)
    print(f"Found {len(run_dirs)} run directories to process")

    if not run_dirs:
        print("No runs found. Make sure metadata.json files exist.")
        return 1

    # Process all runs
    all_results = []

    for i, run_dir in enumerate(run_dirs):
        print(f"[{i+1}/{len(run_dirs)}] Processing {run_dir.relative_to(input_dir)}...")

        path_info = parse_run_path(run_dir, input_dir)
        result = process_run_folder(run_dir)

        if result is None:
            print(f"    SKIP: Could not process")
            continue

        # Merge path info with result (path info takes precedence for model/effort/num)
        result["model"] = path_info["model"] or result["model"]
        result["effort"] = path_info["effort"] or result["effort"]
        result["run"] = path_info["run"]

        all_results.append(result)

        # Print summary for this run
        print(f"    {result['num_valid']}/{result['num_requested']} valid, "
              f"{result['num_unique_valid']} unique, "
              f"{result['num_iterations']} iterations")

    # Generate CSV summary
    csv_path = input_dir / "results.csv"

    fieldnames = [
        "model",
        "effort",
        "num_requested",
        "run",
        "num_valid",
        "num_unique_valid",
        "num_iterations",
        "perfect",
        "completion_tokens",
        "prompt_tokens",
        "total_tokens",
    ]

    with open(csv_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(all_results)

    print(f"\nResults saved to {csv_path}")

    # Print overall summary
    total = len(all_results)
    perfect_runs = sum(1 for r in all_results if r["perfect"])
    total_valid = sum(r["num_valid"] for r in all_results)
    total_unique_valid = sum(r["num_unique_valid"] for r in all_results)
    total_requested = sum(r["num_requested"] for r in all_results)

    print("\n" + "=" * 60)
    print("AGGREGATION SUMMARY")
    print("=" * 60)
    print(f"Total runs:          {total}")
    print(f"Perfect runs:        {perfect_runs} ({100*perfect_runs/total:.1f}%)" if total > 0 else "Perfect runs:        0")
    print(f"Total scenarios:     {total_requested}")
    print(f"Valid scenarios:     {total_valid} ({100*total_valid/total_requested:.1f}%)" if total_requested > 0 else "Valid scenarios:     0")
    print(f"Unique valid:        {total_unique_valid} ({100*total_unique_valid/total_requested:.1f}%)" if total_requested > 0 else "Unique valid:        0")
    print("=" * 60)

    # Print granular summary
    if all_results:
        # Group by model/effort/num
        run_data = defaultdict(lambda: {
            "runs": 0,
            "perfect": 0,
            "total_valid": 0,
            "total_unique_valid": 0,
            "total_requested": 0,
            "total_iterations": 0,
            "total_completion_tokens": 0,
            "canonical_fens": set(),
        })

        for r in all_results:
            key = (r["model"], r["effort"], r["num_requested"])
            run_data[key]["runs"] += 1
            run_data[key]["perfect"] += 1 if r["perfect"] else 0
            run_data[key]["total_valid"] += r["num_valid"]
            run_data[key]["total_unique_valid"] += r["num_unique_valid"]
            run_data[key]["total_requested"] += r["num_requested"]
            run_data[key]["total_iterations"] += r["num_iterations"]
            run_data[key]["total_completion_tokens"] += r["completion_tokens"]
            run_data[key]["canonical_fens"].update(r.get("canonical_fens", []))

        # Print detailed breakdown
        print("\nDETAILED BREAKDOWN (Model / Effort / Num)")
        print("-" * 140)
        print(f"{'Model':<40} {'Effort':<8} {'Num':<5} {'Runs':<6} {'Avg Iter':<10} {'Perfect':<10} {'Valid':<14} {'Unique':<14} {'Avg Tokens':<12}")
        print("-" * 140)

        for (model, effort, num) in sorted(run_data.keys()):
            stats = run_data[(model, effort, num)]
            perfect_pct = 100 * stats["perfect"] / stats["runs"] if stats["runs"] > 0 else 0
            valid_pct = 100 * stats["total_valid"] / stats["total_requested"] if stats["total_requested"] > 0 else 0
            unique_pct = 100 * stats["total_unique_valid"] / stats["total_requested"] if stats["total_requested"] > 0 else 0
            avg_iter = stats["total_iterations"] / stats["runs"] if stats["runs"] > 0 else 0
            avg_tokens = stats["total_completion_tokens"] / stats["runs"] if stats["runs"] > 0 else 0
            print(f"{model:<40} {effort:<8} {num:<5} {stats['runs']:<6} {avg_iter:>8.1f} "
                  f"{stats['perfect']:>3}/{stats['runs']:<3} ({perfect_pct:>5.1f}%) "
                  f"{stats['total_valid']:>3}/{stats['total_requested']:<3} ({valid_pct:>5.1f}%) "
                  f"{stats['total_unique_valid']:>3}/{stats['total_requested']:<3} ({unique_pct:>5.1f}%) "
                  f"{avg_tokens:>10.0f}")

        # Aggregate by model only
        print("\n" + "-" * 140)
        print("AGGREGATE BY MODEL")
        print("-" * 140)

        model_stats = defaultdict(lambda: {
            "runs": 0,
            "perfect": 0,
            "total_valid": 0,
            "total_unique_valid": 0,
            "total_requested": 0,
            "total_iterations": 0,
            "total_completion_tokens": 0,
        })
        for (model, effort, num), stats in run_data.items():
            model_stats[model]["runs"] += stats["runs"]
            model_stats[model]["perfect"] += stats["perfect"]
            model_stats[model]["total_valid"] += stats["total_valid"]
            model_stats[model]["total_unique_valid"] += stats["total_unique_valid"]
            model_stats[model]["total_requested"] += stats["total_requested"]
            model_stats[model]["total_iterations"] += stats["total_iterations"]
            model_stats[model]["total_completion_tokens"] += stats["total_completion_tokens"]

        for model in sorted(model_stats.keys()):
            stats = model_stats[model]
            perfect_pct = 100 * stats["perfect"] / stats["runs"] if stats["runs"] > 0 else 0
            valid_pct = 100 * stats["total_valid"] / stats["total_requested"] if stats["total_requested"] > 0 else 0
            unique_pct = 100 * stats["total_unique_valid"] / stats["total_requested"] if stats["total_requested"] > 0 else 0
            avg_iter = stats["total_iterations"] / stats["runs"] if stats["runs"] > 0 else 0
            avg_tokens = stats["total_completion_tokens"] / stats["runs"] if stats["runs"] > 0 else 0
            print(f"{model:<40} avg iter: {avg_iter:>5.1f} "
                  f"perfect: {stats['perfect']:>3}/{stats['runs']:<3} ({perfect_pct:>5.1f}%) "
                  f"valid: {stats['total_valid']:>3}/{stats['total_requested']:<3} ({valid_pct:>5.1f}%) "
                  f"unique: {stats['total_unique_valid']:>3}/{stats['total_requested']:<3} ({unique_pct:>5.1f}%) "
                  f"avg tokens: {avg_tokens:>8.0f}")

        # Aggregate by effort level
        print("\n" + "-" * 140)
        print("AGGREGATE BY EFFORT")
        print("-" * 140)

        effort_stats = defaultdict(lambda: {
            "runs": 0,
            "perfect": 0,
            "total_valid": 0,
            "total_unique_valid": 0,
            "total_requested": 0,
            "total_iterations": 0,
            "total_completion_tokens": 0,
        })
        for (model, effort, num), stats in run_data.items():
            effort_stats[effort]["runs"] += stats["runs"]
            effort_stats[effort]["perfect"] += stats["perfect"]
            effort_stats[effort]["total_valid"] += stats["total_valid"]
            effort_stats[effort]["total_unique_valid"] += stats["total_unique_valid"]
            effort_stats[effort]["total_requested"] += stats["total_requested"]
            effort_stats[effort]["total_iterations"] += stats["total_iterations"]
            effort_stats[effort]["total_completion_tokens"] += stats["total_completion_tokens"]

        for effort in sorted(effort_stats.keys()):
            stats = effort_stats[effort]
            perfect_pct = 100 * stats["perfect"] / stats["runs"] if stats["runs"] > 0 else 0
            valid_pct = 100 * stats["total_valid"] / stats["total_requested"] if stats["total_requested"] > 0 else 0
            unique_pct = 100 * stats["total_unique_valid"] / stats["total_requested"] if stats["total_requested"] > 0 else 0
            avg_iter = stats["total_iterations"] / stats["runs"] if stats["runs"] > 0 else 0
            avg_tokens = stats["total_completion_tokens"] / stats["runs"] if stats["runs"] > 0 else 0
            print(f"{effort:<40} avg iter: {avg_iter:>5.1f} "
                  f"perfect: {stats['perfect']:>3}/{stats['runs']:<3} ({perfect_pct:>5.1f}%) "
                  f"valid: {stats['total_valid']:>3}/{stats['total_requested']:<3} ({valid_pct:>5.1f}%) "
                  f"unique: {stats['total_unique_valid']:>3}/{stats['total_requested']:<3} ({unique_pct:>5.1f}%) "
                  f"avg tokens: {avg_tokens:>8.0f}")

        # Aggregate by num_requested
        print("\n" + "-" * 140)
        print("AGGREGATE BY NUM REQUESTED")
        print("-" * 140)

        num_stats = defaultdict(lambda: {
            "runs": 0,
            "perfect": 0,
            "total_valid": 0,
            "total_unique_valid": 0,
            "total_requested": 0,
            "total_iterations": 0,
            "total_completion_tokens": 0,
        })
        for (model, effort, num), stats in run_data.items():
            num_stats[num]["runs"] += stats["runs"]
            num_stats[num]["perfect"] += stats["perfect"]
            num_stats[num]["total_valid"] += stats["total_valid"]
            num_stats[num]["total_unique_valid"] += stats["total_unique_valid"]
            num_stats[num]["total_requested"] += stats["total_requested"]
            num_stats[num]["total_iterations"] += stats["total_iterations"]
            num_stats[num]["total_completion_tokens"] += stats["total_completion_tokens"]

        for num in sorted(num_stats.keys(), key=lambda x: int(x) if str(x).isdigit() else 0):
            stats = num_stats[num]
            perfect_pct = 100 * stats["perfect"] / stats["runs"] if stats["runs"] > 0 else 0
            valid_pct = 100 * stats["total_valid"] / stats["total_requested"] if stats["total_requested"] > 0 else 0
            unique_pct = 100 * stats["total_unique_valid"] / stats["total_requested"] if stats["total_requested"] > 0 else 0
            avg_iter = stats["total_iterations"] / stats["runs"] if stats["runs"] > 0 else 0
            avg_tokens = stats["total_completion_tokens"] / stats["runs"] if stats["runs"] > 0 else 0
            print(f"num={num:<37} avg iter: {avg_iter:>5.1f} "
                  f"perfect: {stats['perfect']:>3}/{stats['runs']:<3} ({perfect_pct:>5.1f}%) "
                  f"valid: {stats['total_valid']:>3}/{stats['total_requested']:<3} ({valid_pct:>5.1f}%) "
                  f"unique: {stats['total_unique_valid']:>3}/{stats['total_requested']:<3} ({unique_pct:>5.1f}%) "
                  f"avg tokens: {avg_tokens:>8.0f}")

    return 0


if __name__ == "__main__":
    exit(main())
