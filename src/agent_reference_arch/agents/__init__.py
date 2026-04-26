"""Agent collection for agent_reference_arch."""

from .planner import get_agent as get_planner_agent
from .planner_foundry import create_agent as create_planner_foundry_agent
from .planner_lmstudio import create_agent as create_planner_lmstudio_agent

__all__ = [
	"create_planner_foundry_agent",
	"create_planner_lmstudio_agent",
	"get_planner_agent",
]
