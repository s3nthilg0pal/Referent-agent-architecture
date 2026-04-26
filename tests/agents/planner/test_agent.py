from agent_reference_arch.agents.planner.agent import AGENT_NAME, get_agent


class _FakeClient:
    pass


def test_planner_agent_configuration():
    agent = get_agent(client=_FakeClient())

    assert agent.name == AGENT_NAME
    assert agent.to_dict()["type"] == "agent"

    tool_names = {
        getattr(tool, "name", type(tool).__name__)
        for tool in agent.default_options["tools"]
    }
    assert "plan_outline" in tool_names
