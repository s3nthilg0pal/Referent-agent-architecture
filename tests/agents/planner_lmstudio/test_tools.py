from agent_reference_arch.agents.planner_lmstudio.tools import plan_outline


def test_lmstudio_tool_reuses_outline_behavior():
    steps = plan_outline("launch a project", max_steps=3)

    assert len(steps) == 3
    assert steps[0].startswith("Clarify the scope of launch a project")
