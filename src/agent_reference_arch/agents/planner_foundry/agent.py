from __future__ import annotations

import asyncio
import os
from typing import Any

from agent_framework.foundry import FoundryAgent
from azure.identity import AzureCliCredential
from dotenv import load_dotenv

from .prompts import build_instructions
from .tools import plan_outline

AGENT_NAME = "planner_foundry"
DEFAULT_PROMPT = "Plan a small internal project launch in 5 steps."


def create_agent(
    *,
    project_endpoint: str | None = None,
    agent_name: str | None = None,
    credential: Any | None = None,
) -> FoundryAgent:
    """Create the Foundry-backed planner agent."""

    resolved_project_endpoint = project_endpoint or os.environ["FOUNDRY_PROJECT_ENDPOINT"]
    resolved_agent_name = agent_name or os.environ.get("FOUNDRY_AGENT_NAME", AGENT_NAME)
    resolved_credential = credential if credential is not None else AzureCliCredential()
    return FoundryAgent(
        project_endpoint=resolved_project_endpoint,
        agent_name=resolved_agent_name,
        credential=resolved_credential,
        name=AGENT_NAME,
        description="Planner agent built with the Microsoft Agent Framework Foundry runtime.",
        instructions=build_instructions(),
        tools=[plan_outline],
    )


def get_agent() -> FoundryAgent:
    """Compatibility alias for the agent factory."""

    return create_agent()


async def run_demo(prompt: str | None = None) -> int:
    """Run a one-shot planner demo from the command line."""

    load_dotenv()
    required_env_vars = ["FOUNDRY_PROJECT_ENDPOINT"]
    missing_env_vars = [name for name in required_env_vars if not os.getenv(name)]
    if missing_env_vars:
        missing_text = ", ".join(missing_env_vars)
        print(f"Missing environment variables: {missing_text}")
        print("Set them in your shell or .env file before running the Foundry planner agent.")
        return 2

    agent = get_agent()
    result = await agent.run(prompt or DEFAULT_PROMPT)
    print(result.text)
    return 0


def main() -> None:
    raise SystemExit(asyncio.run(run_demo()))
