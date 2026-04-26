"""Local tools for the planner agent."""

from __future__ import annotations

from agent_framework import tool


@tool
def plan_outline(goal: str, max_steps: int = 5) -> list[str]:
    """Turn a goal into a short numbered action plan."""

    normalized_goal = " ".join(goal.split()).strip()
    if not normalized_goal:
        return ["Clarify the goal before planning."]

    steps = [
        f"Clarify the scope of {normalized_goal}.",
        f"List the key constraints for {normalized_goal}.",
        f"Draft the first version of {normalized_goal}.",
        f"Review risks and dependencies for {normalized_goal}.",
        f"Finalize the next actions for {normalized_goal}.",
    ]
    return steps[: max(1, max_steps)]
