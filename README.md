# agent-reference-arch

A small Python project scaffold managed with [uv](https://docs.astral.sh/uv/).

This repo now includes a planner-style agent package that mirrors the folder-per-agent
pattern used in the Microsoft Agent Framework samples.

## Quick Start

1. Create the environment and install dependencies:

   ```bash
   uv sync
   ```

2. Run the CLI:

   ```bash
   uv run agent-reference-arch
   ```

   Planner variants are available too:

   ```bash
   uv run planner
   uv run planner-foundry
   uv run planner-lmstudio
   uv run agent-gradio
   ```

   The LM Studio variant expects `LM_STUDIO_MODEL` and can use the default
   local OpenAI-compatible endpoint at `http://localhost:1234/v1` with the
   default API key `lm-studio`.

   The Gradio UI lets you pick any planner backend from a browser.

3. Run the tests:

   ```bash
   uv run pytest
   ```

4. Run linting:

   ```bash
   uv run ruff check .
   ```

## Agent Layout

- `src/agent_reference_arch/agents/planner/` contains the Microsoft Agent Framework setup.
- `prompts.py` holds the system instructions.
- `tools.py` holds local function tools.
- `agent.py` builds and runs the agent.

## Planner Demo

Set these environment variables before running the planner:

- `FOUNDRY_PROJECT_ENDPOINT`
- `FOUNDRY_MODEL`

Then start it with:

```bash
uv run planner
```
