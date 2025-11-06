from hanoi import TowerOfHanoiProblem
from search import bfs

def run(n=3, start=0, goal=2):
    problem = TowerOfHanoiProblem(n_disks=n, start_peg=start, goal_peg=goal)
    actions, _ = bfs(problem)
    print(f"Found solution for n={n}: {len(actions)} moves")
    # pretty print
    for k, (i, j) in enumerate(actions, 1):
        print(f"{k:2d}. Move top from peg {i} -> peg {j}")
    return actions

if __name__ == "__main__":
    run(3)
