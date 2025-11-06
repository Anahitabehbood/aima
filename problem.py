from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Iterable, Tuple, List

class Problem(ABC):
    """
    AIMA-style abstract problem.
    Defines the *interface* that search algorithms depend on.
    """
    def __init__(self, initial_state: Any, goal_state: Any | None = None):
        self.initial_state = initial_state
        self.goal_state = goal_state

    @abstractmethod
    def actions(self, state: Any) -> Iterable[Any]:
        """Return iterable of available actions in `state`."""
        ...

    @abstractmethod
    def result(self, state: Any, action: Any) -> Any:
        """Return the new state obtained by applying `action` to `state`."""
        ...

    def goal_test(self, state: Any) -> bool:
        """Return True iff `state` satisfies the goal condition."""
        if self.goal_state is not None:
            return state == self.goal_state
        return False  # override in subclasses if using predicate-style goal

    def step_cost(self, state: Any, action: Any, next_state: Any) -> float:
        """Default unit step cost; override if needed."""
        return 1.0
