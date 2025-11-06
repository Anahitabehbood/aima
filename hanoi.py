from __future__ import annotations
from dataclasses import dataclass
from typing import List, Tuple, Iterable
from state import State
from problem import Problem

Move = Tuple[int, int]  # (from_peg, to_peg)

@dataclass(frozen=True)
class TowerOfHanoiState(State):
    # towers[i] is a tuple of ints; last element is the TOP (smallest index is bottom)
    towers: tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...]]

    def __hash__(self) -> int:
        return hash(self.towers)

    def __eq__(self, other) -> bool:
        return isinstance(other, TowerOfHanoiState) and self.towers == other.towers

    def __repr__(self) -> str:
        return f"Hanoi{self.towers}"

class TowerOfHanoiProblem(Problem):
    """
    Tower of Hanoi as an AIMA-style problem.
    Disks are integers, larger = heavier. Legal move: move top disk to another peg
    with either empty target or larger top disk.
    Goal (default): all disks stacked on peg `goal_peg` in correct order.
    """
    def __init__(self, n_disks: int, start_peg: int = 0, goal_peg: int = 2):
        initial_towers = [[], [], []]
        # bottom -> top: largest -> smallest
        initial_towers[start_peg] = list(range(n_disks, 0, -1))
        initial = TowerOfHanoiState(tuple(tuple(t) for t in initial_towers))
        super().__init__(initial_state=initial, goal_state=None)
        self.goal_peg = goal_peg
        self.n_disks = n_disks

    def actions(self, state: TowerOfHanoiState) -> Iterable[Move]:
        towers = state.towers
        for i in range(3):
            if not towers[i]:
                continue
            disk = towers[i][-1]
            for j in range(3):
                if i == j:
                    continue
                if not towers[j] or towers[j][-1] > disk:
                    yield (i, j)

    def result(self, state: TowerOfHanoiState, action: Move) -> TowerOfHanoiState:
        i, j = action
        towers = [list(t) for t in state.towers]
        disk = towers[i].pop()
        # safety: ensure legal move
        if towers[j] and towers[j][-1] < disk:
            raise ValueError("Illegal move")
        towers[j].append(disk)
        return TowerOfHanoiState(tuple(tuple(t) for t in towers))

    def goal_test(self, state: TowerOfHanoiState) -> bool:
        # All disks must be on goal peg in correct order
        target = tuple(range(self.n_disks, 0, -1))
        return state.towers[self.goal_peg] == target and                all(len(state.towers[p]) == 0 for p in range(3) if p != self.goal_peg)
