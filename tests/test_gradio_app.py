from agent_reference_arch.gradio_app import AGENT_REGISTRY, build_app


def test_gradio_app_registry_contains_all_planner_variants():
    assert set(AGENT_REGISTRY) == {
        "Planner (standard)",
        "Planner (Foundry)",
        "Planner (LM Studio)",
    }


def test_gradio_app_builds_blocks():
    app = build_app()

    assert app.__class__.__name__ == "Blocks"