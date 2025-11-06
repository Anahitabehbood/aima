from __future__ import annotations
from collections import deque
from typing import Any, Callable, Iterable, Tuple, List
from problem import Problem

def bfs(problem: Problem):
    """
    Simple breadth-first search that returns (actions, states) for a shortest solution,
    assuming unit step costs.
    """
    initial = problem.initial_state
    if problem.goal_test(initial):
        return [], [initial]
    frontier = deque([(initial, [])])  # (state, path of actions)
    explored = set([initial])
    while frontier:
        state, actions = frontier.popleft()
        for a in problem.actions(state):
            child = problem.result(state, a)
            if child in explored:
                continue
            new_actions = actions + [a]
            if problem.goal_test(child):
                return new_actions, None  # states path optional
            frontier.append((child, new_actions))
            explored.add(child)
    return None, None  # no solution
