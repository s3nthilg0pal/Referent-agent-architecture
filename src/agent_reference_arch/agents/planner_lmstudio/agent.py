from __future__ import annotations

import asyncio
import os
from typing import Any

from agent_framework import Agent
from agent_framework.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv

from .prompts import build_instructions
from .tools import plan_outline

AGENT_NAME = "planner_lmstudio"
DEFAULT_PROMPT = "Plan a small internal project launch in 5 steps."
DEFAULT_LM_STUDIO_BASE_URL = "http://localhost:1234/v1"
DEFAULT_LM_STUDIO_API_KEY = "lm-studio"


def create_client(
    *,
    model: str | None = None,
    base_url: str | None = None,
    api_key: str | None = None,
) -> OpenAIChatCompletionClient:
    """Create an OpenAI-compatible chat client for LM Studio."""

    resolved_model = model or os.environ["LM_STUDIO_MODEL"]
    resolved_base_url = base_url or os.environ.get(
        "LM_STUDIO_BASE_URL",
        DEFAULT_LM_STUDIO_BASE_URL,
    )
    resolved_api_key = api_key or os.environ.get(
        "LM_STUDIO_API_KEY",
        DEFAULT_LM_STUDIO_API_KEY,
    )
    return OpenAIChatCompletionClient(
        model=resolved_model,
        base_url=resolved_base_url,
        api_key=resolved_api_key,
    )


def create_agent(
    *,
    model: str | None = None,
    base_url: str | None = None,
    api_key: str | None = None,
) -> Agent[Any]:
    """Create the LM Studio-backed planner agent."""

    agent_client = create_client(
        model=model,
        base_url=base_url,
        api_key=api_key,
    )
    return Agent[Any](
        client=agent_client,
        name=AGENT_NAME,
        instructions=build_instructions(),
        tools=[plan_outline],
    )


def get_agent() -> Agent[Any]:
    """Compatibility alias for the agent factory."""

    return create_agent()


async def run_demo(prompt: str | None = None) -> int:
    """Run a one-shot planner demo from the command line."""

    load_dotenv()
    required_env_vars = ["LM_STUDIO_MODEL"]
    missing_env_vars = [name for name in required_env_vars if not os.getenv(name)]
    if missing_env_vars:
        missing_text = ", ".join(missing_env_vars)
        print(f"Missing environment variables: {missing_text}")
        print(
            "Set them in your shell or .env file before running the LM Studio planner agent."
        )
        return 2

    agent = get_agent()
    result = await agent.run(prompt or DEFAULT_PROMPT)
    print(result.text)
    return 0


def main() -> None:
    raise SystemExit(asyncio.run(run_demo()))