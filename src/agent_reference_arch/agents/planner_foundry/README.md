# Planner Foundry agent

This variant mirrors the planner folder layout, but it uses the Microsoft Agent Framework Foundry-native `FoundryAgent` class.

## Files

- `agent.py`: builds the Foundry-backed agent and provides a small CLI demo
- `prompts.py`: system instructions, reused from the base planner
- `tools.py`: local function tools, reused from the base planner
- `__init__.py`: package exports

## Run

Set this environment variable first:

- `FOUNDRY_PROJECT_ENDPOINT`

Then run:

```bash
uv run planner-foundry
```

You can also run the module directly:

```bash
uv run python -m agent_reference_arch.agents.planner_foundry
```
