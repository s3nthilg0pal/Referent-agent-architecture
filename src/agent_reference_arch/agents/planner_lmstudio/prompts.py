"""System instructions for the planner LM Studio agent."""

from agent_reference_arch.agents.planner.prompts import (
    build_instructions as _build_base_instructions,
)


def build_instructions() -> str:
    """Reuse the base planner instructions for the LM Studio variant."""

    return _build_base_instructions()
