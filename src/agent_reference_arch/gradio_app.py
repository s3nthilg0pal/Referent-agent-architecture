from __future__ import annotations

from collections.abc import Callable
from typing import Any

import gradio as gr
from dotenv import load_dotenv

from agent_reference_arch.agents.planner.agent import get_agent as get_planner_agent
from agent_reference_arch.agents.planner_foundry.agent import create_agent as create_foundry_agent
from agent_reference_arch.agents.planner_lmstudio.agent import create_agent as create_lmstudio_agent

AgentFactory = Callable[[], Any]

AGENT_REGISTRY: dict[str, tuple[str, AgentFactory]] = {
    "Planner (standard)": (
        "Direct Agent Framework client",
        get_planner_agent,
    ),
    "Planner (Foundry)": (
        "Microsoft Agent Framework Foundry runtime",
        create_foundry_agent,
    ),
    "Planner (LM Studio)": (
        "Azure OpenAI-compatible LM Studio backend",
        create_lmstudio_agent,
    ),
}


def _format_error(agent_label: str, exc: Exception) -> str:
    return (
        f"### {agent_label}\n\n"
        f"Agent execution failed: `{type(exc).__name__}`\n\n"
        f"{exc}"
    )


async def chat(prompt: str, agent_label: str) -> str:
    load_dotenv()
    prompt = prompt.strip()
    if not prompt:
        return "Please enter a prompt."

    if agent_label not in AGENT_REGISTRY:
        return f"Unknown agent selection: {agent_label}"

    agent_description, agent_factory = AGENT_REGISTRY[agent_label]
    try:
        agent = agent_factory()
        result = await agent.run(prompt)
        output_text = getattr(result, "text", str(result))
    except Exception as exc:  # pragma: no cover - surfaced in the UI
        return _format_error(agent_label, exc)

    return f"### {agent_label}\n{agent_description}\n\n{output_text}"


def build_app() -> gr.Blocks:
    with gr.Blocks(title="Agent Reference Architecture") as demo:
        gr.Markdown(
            "# Agent Reference Architecture\n"
            "Chat with the planner variants through a single Gradio interface."
        )
        agent_label = gr.Dropdown(
            choices=list(AGENT_REGISTRY.keys()),
            value="Planner (LM Studio)",
            label="Agent",
        )
        prompt = gr.Textbox(
            label="Prompt",
            placeholder="Plan a small internal project launch in 5 steps.",
            lines=6,
        )
        submit = gr.Button("Run agent")
        output = gr.Markdown()

        submit.click(
            chat,
            inputs=[prompt, agent_label],
            outputs=output,
            show_progress="full",
        )
        prompt.submit(
            chat,
            inputs=[prompt, agent_label],
            outputs=output,
            show_progress="full",
        )

    return demo.queue()


def main() -> None:
    build_app().launch()