#!/usr/bin/env python3
"""
Streamlit-based viewer for benchmark results.

Usage:
    streamlit run view_results.py -- --results ./results
"""

import argparse
import csv
import json
import re
from pathlib import Path

import streamlit as st


def strip_integrity_attributes(html: str) -> str:
    """Remove integrity attributes from script and link tags."""
    # Remove integrity="..." attributes (handles both single and double quotes)
    html = re.sub(r'\s+integrity\s*=\s*"[^"]*"', '', html)
    html = re.sub(r"\s+integrity\s*=\s*'[^']*'", '', html)
    return html


def replace_chessboard_js(html: str) -> str:
    """Replace chessboard.js references with chessboard-js (fork)."""
    # Replace CDN URLs for chessboard.js with chessboard-js
    # Common patterns:
    # - chessboardjs.com -> chessboard-js (npm package or different CDN)
    # - @chessboard/chessboard.js -> chessboard-js

    # Replace script src references
    html = re.sub(
        r'(https?://[^"\']*?)chessboard\.js([^"\']*\.js)',
        r'\1chessboard-js\2',
        html
    )
    html = re.sub(
        r'(https?://[^"\']*?)chessboardjs([^"\']*)',
        r'\1chessboard-js\2',
        html
    )

    # Replace CSS references
    html = re.sub(
        r'(https?://[^"\']*?)chessboard\.js([^"\']*\.css)',
        r'\1chessboard-js\2',
        html
    )

    # Replace unpkg/cdnjs/jsdelivr specific patterns
    # unpkg.com/@chessboard/chessboard.js -> unpkg.com/chessboard-js
    html = re.sub(
        r'unpkg\.com/@chessboard/chessboard\.js',
        'unpkg.com/chessboard-js',
        html
    )

    # cdnjs chessboard.js patterns
    html = re.sub(
        r'cdnjs\.cloudflare\.com/ajax/libs/chessboard\.js',
        'cdnjs.cloudflare.com/ajax/libs/chessboard-js',
        html
    )

    # jsdelivr patterns
    html = re.sub(
        r'cdn\.jsdelivr\.net/npm/@chessboard/chessboard\.js',
        'cdn.jsdelivr.net/npm/chessboard-js',
        html
    )

    return html

# Must be first Streamlit command
st.set_page_config(page_title="Chess Benchmark Viewer", layout="wide")

# Maximum number of scenarios we support scoring
MAX_SCENARIOS = 10


def find_all_results(results_dir: Path) -> list[dict]:
    """Find all result directories by searching for metadata.json files."""
    results = []

    if not results_dir.exists():
        return results

    # Find all metadata.json files recursively
    for metadata_path in results_dir.rglob("metadata.json"):
        run_dir = metadata_path.parent

        # Validate this is a run directory
        if not run_dir.name.startswith("run_"):
            continue

        try:
            run_num = int(run_dir.name.split("_")[1])
        except (IndexError, ValueError):
            continue

        # Parse the path to extract components
        try:
            num_dir = run_dir.parent
            effort_dir = num_dir.parent
            prompt_dir = effort_dir.parent

            if not num_dir.name.startswith("num_"):
                continue
            if not effort_dir.name.startswith("effort_"):
                continue

            num_val = int(num_dir.name.split("_")[1])
            effort_level = effort_dir.name.replace("effort_", "")

            model_path = prompt_dir.parent.relative_to(results_dir)
            model_name = str(model_path)
            prompt_name = prompt_dir.name

        except (ValueError, IndexError):
            continue

        html_path = run_dir / "app.html"
        reasoning_path = run_dir / "reasoning.md"

        try:
            metadata = json.loads(metadata_path.read_text())
        except json.JSONDecodeError:
            continue

        results.append({
            "path": run_dir,
            "model": model_name,
            "prompt": prompt_name,
            "effort": effort_level,
            "num": num_val,
            "run": run_num,
            "has_html": html_path.exists(),
            "has_reasoning": reasoning_path.exists(),
            "metadata": metadata,
            "id": f"{model_name}|{prompt_name}|{effort_level}|num_{num_val}|run_{run_num}",
        })

    return sorted(
        results,
        key=lambda x: (x["model"], x["prompt"], x["effort"], x["num"], x["run"]),
    )


def load_scores(scores_path: Path) -> dict:
    """Load existing scores from CSV."""
    scores = {}
    if scores_path.exists():
        with open(scores_path, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                score = {
                    "board_correct": row.get("board_correct", "") == "True",
                    "drag_drop_works": row.get("drag_drop_works", "") == "True",
                    "checkmate_logic_valid": row.get("checkmate_logic_valid", "") == "True",
                    "scenarios_distinct": row.get("scenarios_distinct", "") == "True",
                    "needs_integrity_stripped": row.get("needs_integrity_stripped", "") == "True",
                    "needs_chessboard_js_replaced": row.get("needs_chessboard_js_replaced", "") == "True",
                    "notes": row.get("notes", ""),
                }
                # Load individual scenario scores
                for i in range(1, MAX_SCENARIOS + 1):
                    key = f"scenario_{i}_valid"
                    if key in row:
                        score[key] = row[key] == "True"
                scores[row["id"]] = score
    return scores


def save_scores(scores_path: Path, scores: dict, results: list[dict]):
    """Save scores to CSV."""
    scores_path.parent.mkdir(parents=True, exist_ok=True)

    # Build fieldnames dynamically based on max scenarios in results
    max_num = max((r["num"] for r in results), default=3)
    scenario_fields = [f"scenario_{i}_valid" for i in range(1, max_num + 1)]

    fieldnames = [
        "id", "model", "prompt", "effort", "num", "run",
        "board_correct", "drag_drop_works", "checkmate_logic_valid", "scenarios_distinct",
        "needs_integrity_stripped", "needs_chessboard_js_replaced",
    ] + scenario_fields + ["valid_scenario_count", "notes"]

    with open(scores_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        result_lookup = {r["id"]: r for r in results}

        for result_id, score in scores.items():
            if result_id in result_lookup:
                r = result_lookup[result_id]
                row = {
                    "id": result_id,
                    "model": r["model"],
                    "prompt": r["prompt"],
                    "effort": r["effort"],
                    "num": r["num"],
                    "run": r["run"],
                    "board_correct": score.get("board_correct", False),
                    "drag_drop_works": score.get("drag_drop_works", False),
                    "checkmate_logic_valid": score.get("checkmate_logic_valid", False),
                    "scenarios_distinct": score.get("scenarios_distinct", False),
                    "needs_integrity_stripped": score.get("needs_integrity_stripped", False),
                    "needs_chessboard_js_replaced": score.get("needs_chessboard_js_replaced", False),
                    "notes": score.get("notes", ""),
                }
                # Add scenario scores and count valid ones
                valid_count = 0
                for i in range(1, r["num"] + 1):
                    key = f"scenario_{i}_valid"
                    is_valid = score.get(key, False)
                    row[key] = is_valid
                    if is_valid:
                        valid_count += 1
                row["valid_scenario_count"] = valid_count
                writer.writerow(row)


def main():
    parser = argparse.ArgumentParser(description="View benchmark results")
    parser.add_argument(
        "--results", type=str, default="./results", help="Results directory"
    )

    args, _ = parser.parse_known_args()

    results_dir = Path(args.results)
    scores_path = results_dir / "scores.csv"

    results = find_all_results(results_dir)

    if "scores" not in st.session_state:
        st.session_state.scores = load_scores(scores_path)

    st.title("Chess Benchmark Viewer")

    if not results:
        st.warning(f"No results found in {results_dir}")
        st.info("Run `streamlit run view_results.py -- --results ./path/to/results`")
        return

    # Sidebar filters
    st.sidebar.header("Filters")

    models = sorted(set(r["model"] for r in results))
    prompts = sorted(set(r["prompt"] for r in results))
    efforts = sorted(set(r["effort"] for r in results))
    nums = sorted(set(r["num"] for r in results))

    if "filter_init" not in st.session_state:
        st.session_state.filter_init = True
        st.session_state.selected_models = models
        st.session_state.selected_prompts = prompts
        st.session_state.selected_efforts = efforts
        st.session_state.selected_nums = nums

    selected_models = st.sidebar.multiselect(
        "Models", models, default=st.session_state.selected_models
    )
    selected_prompts = st.sidebar.multiselect(
        "Prompts", prompts, default=st.session_state.selected_prompts
    )
    selected_efforts = st.sidebar.multiselect(
        "Effort", efforts, default=st.session_state.selected_efforts
    )
    selected_nums = st.sidebar.multiselect(
        "Num scenarios", nums, default=st.session_state.selected_nums
    )

    only_unscored = st.sidebar.checkbox("Only show unscored", value=False)
    only_with_html = st.sidebar.checkbox("Only show with HTML", value=False)

    if st.sidebar.button("🔄 Reset Filters (Select All)"):
        st.session_state.selected_models = models
        st.session_state.selected_prompts = prompts
        st.session_state.selected_efforts = efforts
        st.session_state.selected_nums = nums
        st.rerun()

    st.sidebar.markdown(f"**Total results in folder: {len(results)}**")

    filtered = [
        r for r in results
        if r["model"] in selected_models
        and r["prompt"] in selected_prompts
        and r["effort"] in selected_efforts
        and r["num"] in selected_nums
        and (not only_with_html or r["has_html"])
        and (not only_unscored or r["id"] not in st.session_state.scores)
    ]

    st.sidebar.markdown(f"**Showing {len(filtered)} / {len(results)} results**")

    scored_count = len([r for r in filtered if r["id"] in st.session_state.scores])
    st.sidebar.markdown(f"**Scored: {scored_count} / {len(filtered)}**")

    if st.sidebar.button("💾 Save Scores to CSV"):
        save_scores(scores_path, st.session_state.scores, results)
        st.sidebar.success(f"Saved to {scores_path}")

    if st.sidebar.button("📊 Show Summary Stats"):
        st.sidebar.markdown("---")
        if st.session_state.scores:
            total = len(st.session_state.scores)
            board_ok = sum(1 for s in st.session_state.scores.values() if s.get("board_correct"))
            drag_ok = sum(1 for s in st.session_state.scores.values() if s.get("drag_drop_works"))
            checkmate_ok = sum(1 for s in st.session_state.scores.values() if s.get("checkmate_logic_valid"))
            distinct_ok = sum(1 for s in st.session_state.scores.values() if s.get("scenarios_distinct"))

            # Count total valid scenarios
            total_scenarios = 0
            valid_scenarios = 0
            for rid, score in st.session_state.scores.items():
                # Find the result to get num
                for r in results:
                    if r["id"] == rid:
                        total_scenarios += r["num"]
                        for i in range(1, r["num"] + 1):
                            if score.get(f"scenario_{i}_valid", False):
                                valid_scenarios += 1
                        break

            st.sidebar.metric("Board Correct", f"{board_ok}/{total} ({100*board_ok/total:.0f}%)")
            st.sidebar.metric("Drag/Drop Works", f"{drag_ok}/{total} ({100*drag_ok/total:.0f}%)")
            st.sidebar.metric("Checkmate Logic Valid", f"{checkmate_ok}/{total} ({100*checkmate_ok/total:.0f}%)")
            st.sidebar.metric("Scenarios Distinct", f"{distinct_ok}/{total} ({100*distinct_ok/total:.0f}%)")
            if total_scenarios > 0:
                st.sidebar.metric("Valid Scenarios", f"{valid_scenarios}/{total_scenarios} ({100*valid_scenarios/total_scenarios:.0f}%)")

    if not filtered:
        st.info("No results match the current filters.")
        return

    # Navigation
    if "current_index" not in st.session_state:
        st.session_state.current_index = 0

    st.session_state.current_index = max(0, min(st.session_state.current_index, len(filtered) - 1))

    col1, col2, col3, col4 = st.columns([1, 1, 2, 1])

    with col1:
        if st.button("⬅️ Previous") and st.session_state.current_index > 0:
            st.session_state.current_index -= 1
            st.rerun()

    with col2:
        if st.button("Next ➡️") and st.session_state.current_index < len(filtered) - 1:
            st.session_state.current_index += 1
            st.rerun()

    with col3:
        jump_to = st.number_input(
            "Jump to",
            min_value=1,
            max_value=len(filtered),
            value=st.session_state.current_index + 1,
            label_visibility="collapsed",
        )
        if jump_to - 1 != st.session_state.current_index:
            st.session_state.current_index = jump_to - 1
            st.rerun()

    with col4:
        st.markdown(f"**{st.session_state.current_index + 1} / {len(filtered)}**")

    current = filtered[st.session_state.current_index]

    st.markdown(f"""
    ### {current['model']}
    **Prompt:** {current['prompt']} | **Effort:** {current['effort']} | **Num:** {current['num']} | **Run:** {current['run']}
    """)

    is_scored = current["id"] in st.session_state.scores
    if is_scored:
        st.success("✓ Scored")

    left_col, right_col = st.columns([3, 1])

    with left_col:
        if current["has_html"]:
            html_path = current["path"] / "app.html"
            html_content = html_path.read_text()

            # Toggle to strip integrity attributes
            strip_integrity = st.checkbox(
                "🔧 Strip integrity attributes (fix CDN loading issues)",
                value=False,
                key=f"strip_integrity_{current['id']}",
            )

            # Toggle to replace chessboard.js with chessboard-js
            use_chessboard_js_fork = st.checkbox(
                "🔄 Replace chessboard.js with chessboard-js (fork)",
                value=False,
                key=f"chessboard_js_fork_{current['id']}",
            )

            if strip_integrity:
                html_content = strip_integrity_attributes(html_content)
                st.info("Integrity attributes stripped from HTML")

            if use_chessboard_js_fork:
                html_content = replace_chessboard_js(html_content)
                st.info("chessboard.js replaced with chessboard-js")

            st.components.v1.html(html_content, height=1000, scrolling=True)
        else:
            st.warning("No HTML file generated for this result.")
            response_path = current["path"] / "response.md"
            if response_path.exists():
                with st.expander("View Response"):
                    st.markdown(response_path.read_text()[:3000] + "...")

    with right_col:
        st.markdown("### Scoring")

        existing = st.session_state.scores.get(current["id"], {})

        # Global checks
        board_correct = st.checkbox(
            "✓ Board rendered correctly",
            value=existing.get("board_correct", False),
            key=f"board_{current['id']}",
        )

        drag_drop_works = st.checkbox(
            "✓ Drag & drop works",
            value=existing.get("drag_drop_works", False),
            key=f"drag_{current['id']}",
        )

        checkmate_logic_valid = st.checkbox(
            "✓ Checkmate logic valid",
            value=existing.get("checkmate_logic_valid", False),
            key=f"checkmate_{current['id']}",
        )

        scenarios_distinct = st.checkbox(
            "✓ Scenarios are distinct",
            value=existing.get("scenarios_distinct", False),
            key=f"distinct_{current['id']}",
        )

        needs_integrity_stripped = st.checkbox(
            "⚠️ Needs integrity stripped",
            value=existing.get("needs_integrity_stripped", False),
            key=f"integrity_{current['id']}",
        )

        needs_chessboard_js_replaced = st.checkbox(
            "⚠️ Needs chessboard-js replaced",
            value=existing.get("needs_chessboard_js_replaced", False),
            key=f"chessboard_replace_{current['id']}",
        )

        # Individual scenario scoring
        st.markdown("---")
        st.markdown(f"**Scenarios (0-{current['num']}):**")

        scenario_values = {}
        cols = st.columns(min(current["num"], 5))  # Max 5 per row
        for i in range(1, current["num"] + 1):
            col_idx = (i - 1) % 5
            with cols[col_idx]:
                key = f"scenario_{i}_valid"
                scenario_values[key] = st.checkbox(
                    f"#{i}",
                    value=existing.get(key, False),
                    key=f"{key}_{current['id']}",
                )

        valid_count = sum(1 for v in scenario_values.values() if v)
        st.markdown(f"**Valid: {valid_count}/{current['num']}**")

        st.markdown("---")
        notes = st.text_area(
            "Notes",
            value=existing.get("notes", ""),
            key=f"notes_{current['id']}",
            height=100,
        )

        # Save button
        if st.button("💾 Save Score", key=f"save_{current['id']}"):
            score_data = {
                "board_correct": board_correct,
                "drag_drop_works": drag_drop_works,
                "checkmate_logic_valid": checkmate_logic_valid,
                "scenarios_distinct": scenarios_distinct,
                "needs_integrity_stripped": needs_integrity_stripped,
                "needs_chessboard_js_replaced": needs_chessboard_js_replaced,
                "notes": notes,
            }
            score_data.update(scenario_values)
            st.session_state.scores[current["id"]] = score_data
            save_scores(scores_path, st.session_state.scores, results)
            st.success("Saved!")
            st.rerun()

        # Quick score buttons
        st.markdown("---")
        st.markdown("**Quick Score:**")

        col_a, col_b = st.columns(2)
        with col_a:
            if st.button("✅ All Good", key=f"allgood_{current['id']}"):
                score_data = {
                    "board_correct": True,
                    "drag_drop_works": True,
                    "checkmate_logic_valid": True,
                    "scenarios_distinct": True,
                    "needs_integrity_stripped": False,
                    "needs_chessboard_js_replaced": False,
                    "notes": "",
                }
                for i in range(1, current["num"] + 1):
                    score_data[f"scenario_{i}_valid"] = True
                st.session_state.scores[current["id"]] = score_data
                save_scores(scores_path, st.session_state.scores, results)
                if st.session_state.current_index < len(filtered) - 1:
                    st.session_state.current_index += 1
                st.rerun()

        with col_b:
            if st.button("❌ All Bad", key=f"allbad_{current['id']}"):
                score_data = {
                    "board_correct": False,
                    "drag_drop_works": False,
                    "checkmate_logic_valid": False,
                    "scenarios_distinct": False,
                    "needs_integrity_stripped": False,
                    "needs_chessboard_js_replaced": False,
                    "notes": "",
                }
                for i in range(1, current["num"] + 1):
                    score_data[f"scenario_{i}_valid"] = False
                st.session_state.scores[current["id"]] = score_data
                save_scores(scores_path, st.session_state.scores, results)
                if st.session_state.current_index < len(filtered) - 1:
                    st.session_state.current_index += 1
                st.rerun()

        # Show reasoning if available
        if current["has_reasoning"]:
            st.markdown("---")
            with st.expander("View Reasoning Trace"):
                reasoning_path = current["path"] / "reasoning.md"
                reasoning = reasoning_path.read_text()
                if len(reasoning) > 10000:
                    st.markdown(reasoning[:10000] + "\n\n... [truncated]")
                else:
                    st.markdown(reasoning)

        with st.expander("Metadata"):
            st.json(current["metadata"])


if __name__ == "__main__":
    main()
