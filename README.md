# Chess behavior benchmarking

Chess endgame benchmark across different language models. The question is: in a task with multiple sub-components ("build me a javascript app to practice chess endgames"), what causes the whole task to fail? We experiment with different approaches to determine this. 

## Claude code folders

- `claude_code_apps` contains the chess endgame practice apps coded up by Claude Code
- `claude_code_transcripts` contains transcripts of Claude Code sessions regarding the chess endgame example

## bench folder

- `bench/run_all.sh` to run the whole suite
- Run `plot_results.R` in R to plot all the relevant plots