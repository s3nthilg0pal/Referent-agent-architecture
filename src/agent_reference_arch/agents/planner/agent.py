from __future__ import annotations

import asyncio
import os
from typing import Any

from agent_framework import Agent
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential
from dotenv import load_dotenv

from .prompts import build_instructions
from .tools import plan_outline

AGENT_NAME = "planner"
DEFAULT_PROMPT = "Plan a small internal project launch in 5 steps."


def create_client() -> FoundryChatClient:
    """Create the Microsoft Agent Framework chat client for this agent."""

    project_endpoint = os.environ["FOUNDRY_PROJECT_ENDPOINT"]
    model = os.environ["FOUNDRY_MODEL"]
    return FoundryChatClient(
        project_endpoint=project_endpoint,
        model=model,
        credential=AzureCliCredential(),
    )


def get_agent(client: Any | None = None) -> Agent[Any]:
    """Create the planner agent."""

    agent_client = client if client is not None else create_client()
    return Agent[Any](
        client=agent_client,
        name=AGENT_NAME,
        instructions=build_instructions(),
        tools=[plan_outline],
    )


async def run_demo(prompt: str | None = None) -> int:
    """Run a one-shot planner demo from the command line."""

    load_dotenv()
    required_env_vars = ["FOUNDRY_PROJECT_ENDPOINT", "FOUNDRY_MODEL"]
    missing_env_vars = [name for name in required_env_vars if not os.getenv(name)]
    if missing_env_vars:
        missing_text = ", ".join(missing_env_vars)
        print(f"Missing environment variables: {missing_text}")
        print("Set them in your shell or .env file before running the planner agent.")
        return 2

    agent = get_agent()
    result = await agent.run(prompt or DEFAULT_PROMPT)
    print(result.text)
    return 0


def main() -> None:
    raise SystemExit(asyncio.run(run_demo()))
