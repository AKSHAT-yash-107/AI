import random
import math

# ─────────────────────────────────────────────
#  N-Queens — Hill Climbing + Random Restarts
# ─────────────────────────────────────────────

def count_attacks(board):
    """Count the number of attacking queen pairs."""
    n = len(board)
    attacks = 0
    for i in range(n):
        for j in range(i + 1, n):
            # Same row or same diagonal
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                attacks += 1
    return attacks


def get_best_neighbor(board):
    """
    Find the neighbor state with the fewest conflicts.
    A neighbor is formed by moving one queen to a different row in its column.
    """
    n = len(board)
    best_board = None
    best_cost = math.inf

    for col in range(n):
        for row in range(n):
            if board[col] == row:
                continue                      # skip current position
            neighbor = board[:]
            neighbor[col] = row
            cost = count_attacks(neighbor)
            if cost < best_cost:
                best_cost = cost
                best_board = neighbor[:]

    return best_board, best_cost


def hill_climbing(n):
    """
    One attempt of hill climbing from a random starting board.
    Returns (board, steps) — board is None if stuck at a local minimum.
    """
    board = [random.randint(0, n - 1) for _ in range(n)]
    steps = 0

    while True:
        current_cost = count_attacks(board)
        if current_cost == 0:
            return board, steps            # solved!

        best_board, best_cost = get_best_neighbor(board)

        if best_cost >= current_cost:
            return None, steps             # local minimum — give up this attempt

        board = best_board
        steps += 1


def hill_climbing_with_restarts(n, max_restarts=1000):
    """
    Repeatedly restart hill climbing until a solution is found.
    Returns (solution_board, total_steps, total_restarts).
    """
    total_steps = 0
    total_restarts = 0

    for _ in range(max_restarts):
        board, steps = hill_climbing(n)
        total_steps += steps
        if board is not None:
            return board, total_steps, total_restarts
        total_restarts += 1

    return None, total_steps, total_restarts   # failed


# ─────────────────────────────────────────────
#  Visualisation helpers
# ─────────────────────────────────────────────

def print_board(board):
    """Print the board as a grid with queens (Q) and dots (.)."""
    n = len(board)
    separator = "+" + ("---+" * n)
    print(separator)
    for row in range(n):
        row_str = "|"
        for col in range(n):
            row_str += " Q |" if board[col] == row else " . |"
        print(row_str)
        print(separator)


def print_solution(n, board, steps, restarts):
    print(f"\n{'='*45}")
    print(f"  N-Queens Hill Climbing  (N = {n})")
    print(f"{'='*45}")
    if board is None:
        print("  ✗  No solution found within the restart limit.")
    else:
        print(f"  ✓  Solution found!")
        print(f"     Steps taken  : {steps}")
        print(f"     Restarts     : {restarts}")
        print(f"     Attacks left : {count_attacks(board)}")
        print(f"     Board repr   : {board}")
        print()
        print_board(board)
    print(f"{'='*45}\n")


# ─────────────────────────────────────────────
#  Demo — solve for several values of N
# ─────────────────────────────────────────────

if __name__ == "__main__":
    for n in [4, 6, 8, 12, 16]:
        board, steps, restarts = hill_climbing_with_restarts(n, max_restarts=2000)
        print_solution(n, board, steps, restarts)