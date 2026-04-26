from agent_reference_arch.agents.planner_foundry.agent import AGENT_NAME, create_agent


class _FakeCredential:
    pass


def test_foundry_agent_configuration():
    agent = create_agent(
        project_endpoint="https://example.invalid",
        agent_name="planner-foundry-test",
        credential=_FakeCredential(),
    )

    assert agent.name == AGENT_NAME
    assert agent.to_dict()["type"] == "foundry_agent"

    tool_names = {
        getattr(tool, "name", type(tool).__name__)
        for tool in agent.default_options["tools"]
    }
    assert "plan_outline" in tool_names
