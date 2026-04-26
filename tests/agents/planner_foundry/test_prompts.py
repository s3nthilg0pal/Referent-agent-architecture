from agent_reference_arch.agents.planner_foundry.prompts import build_instructions


def test_foundry_prompts_reuse_base_instructions():
    instructions = build_instructions()

    assert "# Role" in instructions
    assert "# Workflow" in instructions
