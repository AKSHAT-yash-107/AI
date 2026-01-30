import sys
from typing import List

def visualize_solution(initial_board: List[List[int]], moves: List[str]):
    """
    Visualize the step-by-step solution of the puzzle
    """
    current_board = [row[:] for row in initial_board]
    
    print("=" * 50)
    print("SOLUTION VISUALIZATION")
    print("=" * 50)
    
    print("\nStep 0: Initial State")
    display_board(current_board)
    
    for step, move in enumerate(moves, 1):
        # Find blank position
        blank_pos = find_blank(current_board)
        
        # Apply move
        current_board = apply_move(current_board, blank_pos, move)
        
        print(f"\nStep {step}: Move {move}")
        display_board(current_board)
        print(f"  ({step}/{len(moves)} moves)")

def find_blank(board: List[List[int]]) -> tuple:
    """Find position of blank tile (0)"""
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return (i, j)
    return (0, 0)

def apply_move(board: List[List[int]], blank_pos: tuple, move: str) -> List[List[int]]:
    """Apply a move to the board"""
    new_board = [row[:] for row in board]
    row, col = blank_pos
    
    if move == "Up":
        new_row, new_col = row - 1, col
    elif move == "Down":
        new_row, new_col = row + 1, col
    elif move == "Left":
        new_row, new_col = row, col - 1
    elif move == "Right":
        new_row, new_col = row, col + 1
    else:
        return new_board
    
    # Swap
    new_board[row][col], new_board[new_row][new_col] = \
        new_board[new_row][new_col], new_board[row][col]
    
    return new_board

def display_board(board: List[List[int]]):
    """Display board with nice formatting"""
    print("  ┌───┬───┬───┐")
    for i, row in enumerate(board):
        display_row = "  │"
        for val in row:
            if val == 0:
                display_row += " □ │"
            else:
                display_row += f" {val} │"
        print(display_row)
        if i < 2:
            print("  ├───┼───┼───┤")
    print("  └───┴───┴───┘")

if __name__ == "__main__":
    # Example: Complex puzzle solution
    initial = [
        [7, 2, 4],
        [5, 0, 6],
        [8, 3, 1]
    ]
    
    solution = ["Down", "Right", "Up", "Left", "Left", "Up", "Right", "Right", 
                "Down", "Left", "Down", "Left", "Up", "Right", "Up", "Left", 
                "Down", "Right", "Right", "Down"]
    
    visualize_solution(initial, solution)
