#!/bin/sh
python bench_chess_notation.py --all-models --num 3 --runs 10 --effort high --parallel 8
python bench_chess_notation.py --models anthropic/claude-sonnet-4.5 anthropic/claude-opus-4.5 google/gemini-3-pro-preview openai/gpt-5.1 --num 3 --runs 10 --all-efforts --parallel 8
python bench_chess_notation.py --models anthropic/claude-opus-4.5 google/gemini-3-pro-preview openai/gpt-5.1 --num 10 --runs 10 --effort high --parallel 8
python bench_chess_notation.py --models anthropic/claude-sonnet-4.5 --num 5 10 --runs 10 --effort high --parallel 8
python bench_models.py --models anthropic/claude-sonnet-4.5 anthropic/claude-opus-4.5 google/gemini-3-pro-preview openai/gpt-5.1 --num 3 --runs 10 --effort high --parallel 8
python bench_chess_notation_iterative.py --models anthropic/claude-sonnet-4.5 anthropic/claude-opus-4.5 google/gemini-3-pro-preview openai/gpt-5.1 --num 5 --effort high --runs 5 --max-iterations 10 --parallel 4
python bench_chess_notation_iterative.py --models google/gemini-3-pro-preview openai/gpt-5.1 --num 5 10 --effort high --runs 10 --max-iterations 10 --parallel 4
python validate_chess_notation.py --input results_cn/
python aggregate_cni.py --input results_cni/
python bench_meta.py --num 3 5 7 10 --all-models --num 3 5 7 10 --runs 2 --effort high --parallel 8