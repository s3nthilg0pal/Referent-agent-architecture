"""System instructions for the planner Foundry agent."""

from agent_reference_arch.agents.planner.prompts import (
    build_instructions as _build_base_instructions,
)


def build_instructions() -> str:
    """Reuse the base planner instructions for the Foundry variant."""

    return _build_base_instructions()
