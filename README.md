# Chess endgame benchmarks: extra experiments

This branch is a superset of `main`. The `main` branch holds only the
experiment reported in the *Cognitive Dark Matter* paper: asking frontier
models to build a mate-in-one chess practice app in one shot. This branch adds
three further experiments that probe *why* that task fails, plus additional
Claude Code sessions. None of these extra experiments appear in the paper.

The underlying question: in a task with several sub-components ("build me a
JavaScript app to practice chess endgames"), which component breaks, and can
the model tell?

## Experiments

All benchmark scripts live in `bench/`, call models through
[OpenRouter](https://openrouter.ai), and write one folder per run under
`<results dir>/<provider>/<model>/effort_<effort>/num_<N>/run_<k>/`.

| # | Experiment | Script | Results | Plots |
|---|---|---|---|---|
| 1 | Straight-shot app generation (in paper) | `bench_models.py` | `results/` | 10–14 |
| 2 | Isolated endgame generation in FEN | `bench_chess_notation.py` then `validate_chess_notation.py` | `results_cn/` | 1–9, 15 |
| 3 | Iterated endgame generation with feedback | `bench_chess_notation_iterative.py` then `aggregate_cni.py` | `results_cni/` | 16–18 |
| 4 | Self-prediction of performance (calibration) | `bench_meta.py` | `results_meta/` | 19–22 (saved in `results/`) |

**1. App generation.** Each model is prompted to write a complete drag-and-drop
web app with N mate-in-one scenarios. Runs are scored by hand in the Streamlit
viewer (`view_results.py`), which writes `results/scores.csv` with UI and chess
validity columns. Models: Claude Sonnet 4.5, Claude Opus 4.5, Gemini 3 Pro,
GPT-5.1; 10 runs each at high reasoning effort.

**2. Isolated endgame generation.** Strips away the UI: the model only has to
emit N mate-in-one positions as FEN plus the winning move.
`validate_chess_notation.py` checks each position with the `chess` library
(legal position, move is legal, move gives mate), renders before/after board
PNGs, and writes `results_cn/results.csv`. Swept over reasoning effort
(none/low/medium/high), N (3/5/10) and six models, including Kimi K2 Thinking
and Qwen3-VL.

**3. Iterated generation.** As in 2, but invalid scenarios are reported back
to the model, which regenerates only those while keeping conversation history,
up to 10 iterations. `aggregate_cni.py` checks the final scenarios for
uniqueness (up to board symmetries) and writes `results_cni/results.csv`.

**4. Self-prediction.** Before doing anything, the model is asked what
probability it assigns to producing N valid mate-in-one scenarios.
`results_meta/summary.json` holds the predictions; plots 19–22 compare them to
the observed success rates from experiment 2.

## Running

```sh
cd bench
pip install -r requirements.txt
cp .env.example .env          # then add your OPENROUTER_API_KEY
sh run_all.sh                 # full sweep; expensive
```

Every script accepts `--list-models`, `--models`, `--num`, `--runs`,
`--effort` and `--parallel`; see `run_all.sh` for the exact invocations used.

Plots are made by `plot_results.R`, which must be run from inside `bench/` and
needs the R packages `tidyverse` and `jsonlite`. Plots 1–9 and 15 are written
to `results_cn/`, 16–18 to `results_cni/`, and 10–14 and 19–22 to `results/`.

To browse the generated apps interactively:

```sh
streamlit run view_results.py -- --results ./results
```

## Claude Code folders

- `claude_code_apps/` holds the apps produced in interactive Claude Code
  sessions: Sonnet 4.5 and Opus 4.5 (two runs, November 2025) and Opus 4.6
  (two runs, February 2026, one of them in plan mode).
- `claude_code_transcripts/` holds the matching session transcripts in a
  compact CLI-style format. `format_transcript.py` converts a raw Claude Code
  session `.jsonl` into that format.

## Other files

- `verify_mate.py` (repo root) is a standalone checker used when scoring apps
  by hand: it validates a FEN position and a claimed mate-in-one move with the
  `chess` library and renders the board to PNG.
