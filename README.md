# AIMA – HW2: Problem Formulation (Tower of Hanoi)

**Student:** Anahita Behbood — **ID:** 40236282  
**Course:** Artificial Intelligence — **Homework:** HW2

This repository implements the classic AIMA-style problem abstraction plus a concrete
`TowerOfHanoiProblem`.

## Structure
- `state.py` – abstract `State` interface (hashable/eq/repr).
- `problem.py` – abstract `Problem` with `actions(state)`, `result(state, action)`, `goal_test(state)`.
- `hanoi.py` – `TowerOfHanoiState` and `TowerOfHanoiProblem` (goal peg configurable).
- `search.py` – tiny BFS to demonstrate that the interface works.
- `main.py` – example runner for `n=3` disks.

## Why this matches the prompt
- Abstract **State** ✅
- Abstract **Problem** with *initial state*, *goal test*, *successor generation via `actions`*, and **`result`** ✅
- **Specific Tower of Hanoi class** inheriting from Problem ✅

## Run
```bash
python3 -m venv .venv && . .venv/bin/activate
python -m pip install --upgrade pip
python main.py
```

## Expected output (n=3)
```
Found solution for n=3: 7 moves
 1. Move top from peg 0 -> peg 2
 2. Move top from peg 0 -> peg 1
 3. Move top from peg 2 -> peg 1
 4. Move top from peg 0 -> peg 2
 5. Move top from peg 1 -> peg 0
 6. Move top from peg 1 -> peg 2
 7. Move top from peg 0 -> peg 2
```

## Notes
- We keep states immutable (`dataclass(frozen=True)` + tuples) so they are hashable for explored sets.
- `goal_test` checks that all disks are on the goal peg in descending order, and other pegs are empty.
- You can change `n`, `start`, and `goal` in `main.py`.
