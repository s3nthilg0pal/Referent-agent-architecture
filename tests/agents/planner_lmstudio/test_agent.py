from agent_reference_arch.agents.planner_lmstudio.agent import AGENT_NAME, create_agent


class _FakeAsyncClient:
    pass


def test_lmstudio_agent_configuration():
    agent = create_agent(
        model="local-model",
        base_url="http://localhost:1234/v1",
        api_key="lm-studio",
        async_client=_FakeAsyncClient(),
    )

    assert agent.name == AGENT_NAME
    assert agent.to_dict()["type"] == "agent"

    tool_names = {
        getattr(tool, "name", type(tool).__name__)
        for tool in agent.default_options["tools"]
    }
    assert "plan_outline" in tool_names
