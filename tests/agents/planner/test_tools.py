from agent_reference_arch.agents.planner.tools import plan_outline


def test_plan_outline_returns_numbered_steps():
    steps = plan_outline("launch a small internal project", max_steps=3)

    assert len(steps) == 3
    assert steps[0].startswith("Clarify the scope of launch a small internal project")
    assert all(step.endswith(".") for step in steps)
