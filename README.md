# Who Does the Agent Believe? Source Trust in Interactive Clinical Agents

CS 6180 Final Project (Fall 2026).

## Setup
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # then add your OpenRouter key
```

## Structure
- `data/` fact sheets and corruption specs (MedQA raw data is not committed)
- `prompts/` all prompts, versioned as text files
- `src/env/` corruption injector, patient simulator, tools
- `src/agent/` doctor agent loop and strategies
- `src/eval/` judge, metrics, statistics
- `src/llm.py` OpenRouter gateway with caching
- `results/` run logs, tables, figures

## Reproduce
`python -m src.run_experiment --config configs/experiment.yaml`
