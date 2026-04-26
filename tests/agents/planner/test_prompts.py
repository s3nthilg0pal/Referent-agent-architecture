from agent_reference_arch.agents.planner.prompts import build_instructions


def test_planner_instructions_include_core_sections():
    instructions = build_instructions()

    assert "# Role" in instructions
    assert "# Rules" in instructions
    assert "# Tools" in instructions
    assert "# Workflow" in instructions
    assert "plan_outline" in instructions
