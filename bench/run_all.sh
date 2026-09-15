#!/bin/sh
python bench_models.py --models anthropic/claude-sonnet-4.5 anthropic/claude-opus-4.5 google/gemini-3-pro-preview openai/gpt-5.1 --num 3 --runs 10 --effort high --parallel 8
