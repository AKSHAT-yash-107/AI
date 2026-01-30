"""
Custom Test Cases for 8-Puzzle Solver
Run specific puzzles or create your own test cases
"""

import sys
sys.path.insert(0, '/home/claude')

# Import with proper handling of numeric module name
import importlib.util
spec = importlib.util.spec_from_file_location("puzzle_solver", "/home/claude/8_puzzle_solver.py")
puzzle_solver = importlib.util.module_from_spec(spec)
spec.loader.exec_module(puzzle_solver)

PuzzleState = puzzle_solver.PuzzleState
AStarSolver = puzzle_solver.AStarSolver
Heuristics = puzzle_solver.Heuristics
compare_heuristics = puzzle_solver.compare_heuristics


def test_single_puzzle(initial_board, goal_board, description="Custom Puzzle"):
    """Test a single puzzle configuration"""
    print("\n" + "=" * 70)
    print(f"Testing: {description}")
    print("=" * 70)
    
    compare_heuristics(initial_board, goal_board)


def test_worst_case():
    """Test one of the worst-case scenarios for 8-puzzle"""
    print("\n" + "█" * 70)
    print("WORST CASE SCENARIO - Maximum 31 moves")
    print("█" * 70)
    
    # One of the hardest configurations
    initial = [
        [8, 6, 7],
        [2, 5, 4],
        [3, 0, 1]
    ]
    
    goal = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]
    
    compare_heuristics(initial, goal)


def test_already_solved():
    """Test when puzzle is already at goal state"""
    print("\n" + "█" * 70)
    print("EDGE CASE - Already Solved")
    print("█" * 70)
    
    state = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]
    
    compare_heuristics(state, state)


def test_one_move():
    """Test puzzle requiring only one move"""
    print("\n" + "█" * 70)
    print("SIMPLE CASE - One Move")
    print("█" * 70)
    
    initial = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 0, 8]
    ]
    
    goal = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]
    
    compare_heuristics(initial, goal)


def test_custom_puzzle():
    """
    Create your own puzzle here!
    Make sure the puzzle is solvable (not all configurations are solvable)
    """
    print("\n" + "█" * 70)
    print("CUSTOM PUZZLE - User Defined")
    print("█" * 70)
    
    # Modify these boards to test your own puzzle
    initial = [
        [2, 8, 3],
        [1, 6, 4],
        [7, 0, 5]
    ]
    
    goal = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]
    
    compare_heuristics(initial, goal)


def is_solvable(board):
    """
    Check if a puzzle configuration is solvable
    A puzzle is solvable if the number of inversions is even
    """
    # Flatten the board and remove blank (0)
    flat = []
    for row in board:
        for val in row:
            if val != 0:
                flat.append(val)
    
    # Count inversions
    inversions = 0
    for i in range(len(flat)):
        for j in range(i + 1, len(flat)):
            if flat[i] > flat[j]:
                inversions += 1
    
    return inversions % 2 == 0


def verify_puzzle(board):
    """Verify if a puzzle configuration is valid and solvable"""
    # Check if all numbers 0-8 are present
    numbers = set()
    for row in board:
        for val in row:
            if val < 0 or val > 8:
                return False, "Invalid tile value (must be 0-8)"
            numbers.add(val)
    
    if len(numbers) != 9:
        return False, "Missing or duplicate tiles"
    
    if not is_solvable(board):
        return False, "Configuration is not solvable"
    
    return True, "Valid and solvable"


def interactive_mode():
    """Interactive mode to create and solve custom puzzles"""
    print("\n" + "=" * 70)
    print("INTERACTIVE MODE")
    print("=" * 70)
    print("\nCreate your own 8-puzzle to solve!")
    print("Enter the puzzle row by row, using 0 for the blank tile.")
    print("Example: 1 2 3")
    print()
    
    initial = []
    print("Enter initial state:")
    for i in range(3):
        while True:
            try:
                row_input = input(f"  Row {i+1}: ")
                row = [int(x) for x in row_input.split()]
                if len(row) != 3:
                    print("  Error: Must enter exactly 3 numbers")
                    continue
                initial.append(row)
                break
            except ValueError:
                print("  Error: Please enter valid numbers")
    
    # Verify the puzzle
    valid, message = verify_puzzle(initial)
    if not valid:
        print(f"\n✗ Error: {message}")
        print("Please try again with a valid configuration.")
        return
    
    print(f"\n✓ {message}")
    
    # Use standard goal state
    goal = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]
    
    compare_heuristics(initial, goal)


def benchmark_suite():
    """Run a comprehensive benchmark suite"""
    print("\n" + "█" * 70)
    print("COMPREHENSIVE BENCHMARK SUITE")
    print("█" * 70)
    
    test_cases = [
        {
            'name': 'Trivial (0 moves)',
            'initial': [[1, 2, 3], [4, 5, 6], [7, 8, 0]],
            'goal': [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        },
        {
            'name': 'Very Easy (1 move)',
            'initial': [[1, 2, 3], [4, 5, 6], [7, 0, 8]],
            'goal': [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        },
        {
            'name': 'Easy (4 moves)',
            'initial': [[1, 2, 3], [4, 0, 5], [7, 8, 6]],
            'goal': [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        },
        {
            'name': 'Medium (10 moves)',
            'initial': [[1, 2, 3], [4, 5, 6], [0, 7, 8]],
            'goal': [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        },
        {
            'name': 'Hard (18 moves)',
            'initial': [[2, 8, 3], [1, 6, 4], [7, 0, 5]],
            'goal': [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        },
    ]
    
    total_h1_nodes = 0
    total_h2_nodes = 0
    
    for i, test in enumerate(test_cases, 1):
        print(f"\n{'='*70}")
        print(f"Benchmark {i}/{len(test_cases)}: {test['name']}")
        print(f"{'='*70}")
        
        # Solve with H1
        solver_h1 = AStarSolver(Heuristics.h1_misplaced_tiles)
        _, stats_h1 = solver_h1.solve(
            PuzzleState(test['initial']), 
            PuzzleState(test['goal'])
        )
        
        # Solve with H2
        solver_h2 = AStarSolver(Heuristics.h2_manhattan_distance)
        _, stats_h2 = solver_h2.solve(
            PuzzleState(test['initial']), 
            PuzzleState(test['goal'])
        )
        
        total_h1_nodes += stats_h1['nodes_explored']
        total_h2_nodes += stats_h2['nodes_explored']
        
        print(f"H1: {stats_h1['nodes_explored']} nodes, {stats_h1['solution_depth']} moves")
        print(f"H2: {stats_h2['nodes_explored']} nodes, {stats_h2['solution_depth']} moves")
    
    print(f"\n{'='*70}")
    print("BENCHMARK SUMMARY")
    print(f"{'='*70}")
    print(f"Total nodes explored (H1): {total_h1_nodes}")
    print(f"Total nodes explored (H2): {total_h2_nodes}")
    improvement = ((total_h1_nodes - total_h2_nodes) / total_h1_nodes * 100)
    print(f"H2 improvement: {improvement:.1f}% fewer nodes")


def main():
    """Main menu for custom tests"""
    print("\n" + "█" * 70)
    print("8-PUZZLE SOLVER - CUSTOM TEST SUITE")
    print("█" * 70)
    print("\nAvailable Tests:")
    print("  1. Already Solved (0 moves)")
    print("  2. One Move")
    print("  3. Custom Puzzle")
    print("  4. Worst Case (hardest configuration)")
    print("  5. Interactive Mode (create your own)")
    print("  6. Benchmark Suite (comprehensive tests)")
    print("  7. Run All Tests")
    
    choice = input("\nSelect test (1-7): ").strip()
    
    if choice == '1':
        test_already_solved()
    elif choice == '2':
        test_one_move()
    elif choice == '3':
        test_custom_puzzle()
    elif choice == '4':
        test_worst_case()
    elif choice == '5':
        interactive_mode()
    elif choice == '6':
        benchmark_suite()
    elif choice == '7':
        test_already_solved()
        test_one_move()
        test_custom_puzzle()
        test_worst_case()
        benchmark_suite()
    else:
        print("Invalid choice. Running default tests...")
        test_one_move()


if __name__ == "__main__":
    main()
