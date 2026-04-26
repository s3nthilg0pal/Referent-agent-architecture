# Planner agent

This folder mirrors the agent-per-folder layout used in the Microsoft Agent Framework samples.

## Files

- `agent.py`: builds the agent and provides a small CLI demo
- `prompts.py`: system instructions for the agent
- `tools.py`: local function tools exposed to the agent
- `__main__.py`: module entry point for `python -m`

## Run

Set these environment variables first:

- `FOUNDRY_PROJECT_ENDPOINT`
- `FOUNDRY_MODEL`

Then run:

```bash
uv run planner
```

You can also run the module directly:

```bash
uv run python -m agent_reference_arch.agents.planner
```
