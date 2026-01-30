import heapq
import matplotlib.pyplot as plt
from copy import deepcopy

# ---------------- GOAL STATE ----------------
GOAL = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 0)
)

MOVES = [(-1,0),(1,0),(0,-1),(0,1)]


# ---------------- NODE CLASS ----------------
class Node:
    def __init__(self, state, g, h):
        self.state = state
        self.g = g
        self.h = h
        self.f = g + h

    def __lt__(self, other):
        return self.f < other.f


# ---------------- HEURISTICS ----------------
def h1_misplaced(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != GOAL[i][j]:
                count += 1
    return count


def h2_manhattan(state):
    dist = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                gx = (val - 1) // 3
                gy = (val - 1) % 3
                dist += abs(i - gx) + abs(j - gy)
    return dist


# ---------------- UTILITIES ----------------
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


def neighbors(state):
    x, y = find_blank(state)
    result = []

    for dx, dy in MOVES:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new = [list(row) for row in state]
            new[x][y], new[nx][ny] = new[nx][ny], new[x][y]
            result.append(tuple(tuple(r) for r in new))

    return result


# ---------------- A* SEARCH ----------------
def astar(start, heuristic):
    pq = []
    visited = set()

    h = heuristic(start)
    heapq.heappush(pq, Node(start, 0, h))
    nodes_explored = 0

    while pq:
        current = heapq.heappop(pq)
        nodes_explored += 1

        if current.state == GOAL:
            return current.g, nodes_explored

        visited.add(current.state)

        for n in neighbors(current.state):
            if n not in visited:
                heapq.heappush(
                    pq,
                    Node(n, current.g + 1, heuristic(n))
                )

    return -1, nodes_explored


# ---------------- MAIN ----------------
if __name__ == "__main__":

    start = (
        (1, 2, 3),
        (4, 0, 6),
        (7, 5, 8)
    )

    depth_h1, nodes_h1 = astar(start, h1_misplaced)
    depth_h2, nodes_h2 = astar(start, h2_manhattan)

    print("H1 (Misplaced Tiles)")
    print("Depth:", depth_h1, "Nodes Explored:", nodes_h1)

    print("\nH2 (Manhattan Distance)")
    print("Depth:", depth_h2, "Nodes Explored:", nodes_h2)

    # ---------------- PLOT ----------------
    heuristics = ["H1: Misplaced Tiles", "H2: Manhattan Distance"]
    nodes = [nodes_h1, nodes_h2]
    depths = [depth_h1, depth_h2]

    plt.figure(figsize=(10,4))

    plt.subplot(1,2,1)
    plt.bar(heuristics, nodes)
    plt.ylabel("Nodes Explored")
    plt.title("A* Nodes Explored")
    plt.grid(True)

    plt.subplot(1,2,2)
    plt.bar(heuristics, depths)
    plt.ylabel("Solution Depth")
    plt.title("Solution Depth Comparison")
    plt.grid(True)

    plt.tight_layout()
    plt.show()
