from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List, Optional, Any

from ..tasks.base import Task
from ..tools.base import Tool


class Agent(ABC):
    """Abstract base class representing an autonomous agent."""

    def __init__(self, role: str, goal: str, tools: Optional[List[Tool]] = None) -> None:
        """Initialize the agent.

        Parameters
        ----------
        role: str
            The role assigned to the agent.
        goal: str
            The agent's overall objective.
        tools: list[Tool] | None
            Optional list of tools this agent can utilize.
        """
        self.role = role
        self.goal = goal
        self.tools: List[Tool] = tools or []

    @abstractmethod
    def act(self, task: Task) -> Any:
        """Execute the given task and return a result."""
        raise NotImplementedError
