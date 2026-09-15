# Chess endgame benchmark

Code and results for the chess endgame example in *Cognitive Dark Matter:
Measuring What AI Misses*. Frontier models are asked, in a single prompt, to
build a JavaScript app for practicing three mate-in-one chess endgames with
drag-and-drop pieces. Models reliably produce a working board and UI while
proposing positions that are illegal or not mate-in-one, and never use the
chess libraries they import to check their own positions.

Further experiments that dissect this failure (generating positions in FEN
without a UI, iterated generation with feedback, and asking models to predict
their own success) live on the `extra_experiments` branch.

## Layout

- `bench/bench_models.py` prompts models through
  [OpenRouter](https://openrouter.ai) and writes one folder per run under
  `bench/results/<provider>/<model>/standard/effort_high/num_3/run_<k>/`,
  containing the extracted `app.html`, the raw API response, the model's
  reasoning, and token usage metadata. `bench/results/summary.json` indexes
  all runs.
- `bench/view_results.py` is a Streamlit viewer for opening each generated app
  and scoring it by hand. Scores go to `bench/results/scores.csv` with one row
  per run: board renders, drag-and-drop works, checkmate logic valid,
  scenarios distinct, and per-scenario position validity.
- `bench/plot_results.R` turns `scores.csv` into `bench/results/plot10` to
  `plot14`.
- `verify_mate.py` validates a FEN position and a claimed mate-in-one move
  with the `chess` library and renders the board to PNG. It was used when
  scoring positions by hand.
- `claude_code_apps/` and `claude_code_transcripts/` hold the apps and
  session transcripts from interactive Claude Code runs (Sonnet 4.5 and Opus
  4.5), including sessions where we gave iterative feedback to try to trigger
  self-verification.

## Models and settings

Claude Sonnet 4.5, Claude Opus 4.5, Gemini 3 Pro and GPT-5.1, each run 10
times with the `standard` prompt at high reasoning effort and default sampling
(temperature 1.0, top-p 1.0). The exact prompt is in `PROMPT_TEMPLATES` in
`bench_models.py`.

## Reproducing

```sh
cd bench
pip install -r requirements.txt
cp .env.example .env          # then add your OPENROUTER_API_KEY
sh run_all.sh                 # regenerate the 40 apps
streamlit run view_results.py -- --results ./results   # score them
Rscript plot_results.R        # plots; needs the tidyverse
```

Run the R script from inside `bench/`, since paths are relative to it.
