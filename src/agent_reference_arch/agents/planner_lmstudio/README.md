# Planner LM Studio agent

This variant keeps the planner folder shape, but it connects through the Microsoft Agent Framework OpenAI client with Azure OpenAI-style settings. That makes it easy to point at a local LM Studio server.

## Files

- `agent.py`: builds the OpenAI-based agent and provides a small CLI demo
- `prompts.py`: system instructions, reused from the base planner
- `tools.py`: local function tools, reused from the base planner
- `__init__.py`: package exports

## Run

Set these environment variables first:

- `LM_STUDIO_MODEL`
- `LM_STUDIO_BASE_URL` or the default `http://localhost:1234/v1`
- `LM_STUDIO_API_KEY` or the default `lm-studio`

Then run:

```bash
uv run planner-lmstudio
```

You can also run the module directly:

```bash
uv run python -m agent_reference_arch.agents.planner_lmstudio
```
