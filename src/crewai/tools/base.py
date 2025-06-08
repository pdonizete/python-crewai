<<<<<<< HEAD
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class Tool(ABC):
    """Base class for pluggable tools available to agents."""

    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def use(self, *args: Any, **kwargs: Any) -> Any:
        """Invoke the tool and return a result."""
        raise NotImplementedError
=======
# Placeholder for tool definitions
>>>>>>> main
