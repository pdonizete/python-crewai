from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class Task(ABC):
    """Generic task interface that agents can perform."""

    def __init__(self, description: str) -> None:
        self.description = description

    @abstractmethod
    def execute(self) -> Any:
        """Run the task and return a result."""
        raise NotImplementedError
