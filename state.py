from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Iterable, Any

class State(ABC):
    """
    Abstract base class for a state in a search space.
    Subclasses should be immutable (or treated as such) and hashable
    if used inside search algorithms that keep explored sets.
    """
    @abstractmethod
    def __hash__(self) -> int: ...
    @abstractmethod
    def __eq__(self, other: Any) -> bool: ...
    @abstractmethod
    def __repr__(self) -> str: ...
