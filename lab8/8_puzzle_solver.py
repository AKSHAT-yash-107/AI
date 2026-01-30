import heapq
from typing import List, Tuple, Optional, Set
import time

class PuzzleState:
    """Represents a state of the 8-puzzle"""
    
    def __init__(self, board: List[List[int]], parent=None, move: str = "", g: int = 0):
        self.board = board
        self.parent = parent
        self.move = move
        self.g = g  # Cost from start to current node
        self.h = 0  # Heuristic cost
        self.f = 0  # Total cost (g + h)
        self.blank_pos = self._find_blank()
    
    def _find_blank(self) -> Tuple[int, int]:
        """Find the position of the blank tile (0)"""
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return (i, j)
        return (0, 0)
    
    def __lt__(self, other):
        """Compare states based on f value for priority queue"""
        return self.f < other.f
    
    def __eq__(self, other):
        """Check if two states are equal"""
        return self.board == other.board
    
    def __hash__(self):
        """Hash function for set membership"""
        return hash(str(self.board))
    
    def get_tuple_representation(self) -> tuple:
        """Convert board to tuple for use in visited set"""
        return tuple(tuple(row) for row in self.board)
    
    def is_goal(self, goal_state) -> bool:
        """Check if current state matches goal state"""
        return self.board == goal_state.board
    
    def get_neighbors(self) -> List['PuzzleState']:
        """Generate all possible next states"""
        neighbors = []
        row, col = self.blank_pos
        
        # Possible moves: Up, Down, Left, Right
        moves = [
            (-1, 0, "Up"),
            (1, 0, "Down"),
            (0, -1, "Left"),
            (0, 1, "Right")
        ]
        
        for dr, dc, move_name in moves:
            new_row, new_col = row + dr, col + dc
            
            # Check if move is valid
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                # Create new board by swapping
                new_board = [row[:] for row in self.board]
                new_board[row][col], new_board[new_row][new_col] = \
                    new_board[new_row][new_col], new_board[row][col]
                
                neighbors.append(PuzzleState(new_board, self, move_name, self.g + 1))
        
        return neighbors
    
    def display(self):
        """Display the board in a readable format"""
        for row in self.board:
            print(" ".join(str(x) if x != 0 else "_" for x in row))
        print()


class Heuristics:
    """Heuristic functions for A* search"""
    
    @staticmethod
    def h1_misplaced_tiles(state: PuzzleState, goal_state: PuzzleState) -> int:
        """
        H1: Count the number of misplaced tiles
        (excluding the blank tile)
        """
        count = 0
        for i in range(3):
            for j in range(3):
                if state.board[i][j] != 0 and state.board[i][j] != goal_state.board[i][j]:
                    count += 1
        return count
    
    @staticmethod
    def h2_manhattan_distance(state: PuzzleState, goal_state: PuzzleState) -> int:
        """
        H2: Sum of Manhattan distances of all tiles from their goal positions
        Manhattan distance = |x1 - x2| + |y1 - y2|
        """
        distance = 0
        
        # Create a mapping of tile value to goal position
        goal_positions = {}
        for i in range(3):
            for j in range(3):
                if goal_state.board[i][j] != 0:
                    goal_positions[goal_state.board[i][j]] = (i, j)
        
        # Calculate Manhattan distance for each tile
        for i in range(3):
            for j in range(3):
                tile = state.board[i][j]
                if tile != 0:  # Ignore blank tile
                    goal_i, goal_j = goal_positions[tile]
                    distance += abs(i - goal_i) + abs(j - goal_j)
        
        return distance


class AStarSolver:
    """A* search algorithm implementation"""
    
    def __init__(self, heuristic_func):
        self.heuristic_func = heuristic_func
        self.nodes_explored = 0
        self.max_frontier_size = 0
    
    def solve(self, initial_state: PuzzleState, goal_state: PuzzleState) -> Tuple[Optional[List[str]], dict]:
        """
        Solve the puzzle using A* search
        Returns: (solution path, statistics)
        """
        start_time = time.time()
        
        # Initialize
        initial_state.h = self.heuristic_func(initial_state, goal_state)
        initial_state.f = initial_state.g + initial_state.h
        
        # Priority queue (min-heap)
        frontier = []
        heapq.heappush(frontier, initial_state)
        
        # Visited states
        visited = set()
        visited.add(initial_state.get_tuple_representation())
        
        self.nodes_explored = 0
        self.max_frontier_size = 1
        
        while frontier:
            # Track maximum frontier size
            self.max_frontier_size = max(self.max_frontier_size, len(frontier))
            
            # Get state with lowest f value
            current_state = heapq.heappop(frontier)
            self.nodes_explored += 1
            
            # Check if goal reached
            if current_state.is_goal(goal_state):
                end_time = time.time()
                path = self._reconstruct_path(current_state)
                
                stats = {
                    'nodes_explored': self.nodes_explored,
                    'solution_depth': len(path),
                    'max_frontier_size': self.max_frontier_size,
                    'time_taken': end_time - start_time
                }
                
                return path, stats
            
            # Explore neighbors
            for neighbor in current_state.get_neighbors():
                neighbor_tuple = neighbor.get_tuple_representation()
                
                if neighbor_tuple not in visited:
                    visited.add(neighbor_tuple)
                    neighbor.h = self.heuristic_func(neighbor, goal_state)
                    neighbor.f = neighbor.g + neighbor.h
                    heapq.heappush(frontier, neighbor)
        
        # No solution found
        end_time = time.time()
        stats = {
            'nodes_explored': self.nodes_explored,
            'solution_depth': 0,
            'max_frontier_size': self.max_frontier_size,
            'time_taken': end_time - start_time
        }
        return None, stats
    
    def _reconstruct_path(self, state: PuzzleState) -> List[str]:
        """Reconstruct the path from initial to goal state"""
        path = []
        current = state
        
        while current.parent is not None:
            path.append(current.move)
            current = current.parent
        
        path.reverse()
        return path


def compare_heuristics(initial_board: List[List[int]], goal_board: List[List[int]]):
    """Compare the performance of both heuristics"""
    
    print("=" * 70)
    print("8-PUZZLE SOLVER - A* SEARCH COMPARISON")
    print("=" * 70)
    
    print("\nInitial State:")
    initial_state = PuzzleState(initial_board)
    initial_state.display()
    
    print("Goal State:")
    goal_state = PuzzleState(goal_board)
    goal_state.display()
    
    # Solve with H1 (Misplaced Tiles)
    print("-" * 70)
    print("HEURISTIC 1: Misplaced Tiles")
    print("-" * 70)
    
    solver_h1 = AStarSolver(Heuristics.h1_misplaced_tiles)
    solution_h1, stats_h1 = solver_h1.solve(
        PuzzleState(initial_board), 
        PuzzleState(goal_board)
    )
    
    if solution_h1:
        print(f"✓ Solution found!")
        print(f"  Nodes explored: {stats_h1['nodes_explored']}")
        print(f"  Solution depth: {stats_h1['solution_depth']} moves")
        print(f"  Max frontier size: {stats_h1['max_frontier_size']}")
        print(f"  Time taken: {stats_h1['time_taken']:.4f} seconds")
        print(f"  Solution path: {' → '.join(solution_h1)}")
    else:
        print("✗ No solution found")
    
    # Solve with H2 (Manhattan Distance)
    print("\n" + "-" * 70)
    print("HEURISTIC 2: Manhattan Distance")
    print("-" * 70)
    
    solver_h2 = AStarSolver(Heuristics.h2_manhattan_distance)
    solution_h2, stats_h2 = solver_h2.solve(
        PuzzleState(initial_board), 
        PuzzleState(goal_board)
    )
    
    if solution_h2:
        print(f"✓ Solution found!")
        print(f"  Nodes explored: {stats_h2['nodes_explored']}")
        print(f"  Solution depth: {stats_h2['solution_depth']} moves")
        print(f"  Max frontier size: {stats_h2['max_frontier_size']}")
        print(f"  Time taken: {stats_h2['time_taken']:.4f} seconds")
        print(f"  Solution path: {' → '.join(solution_h2)}")
    else:
        print("✗ No solution found")
    
    # Comparison
    if solution_h1 and solution_h2:
        print("\n" + "=" * 70)
        print("PERFORMANCE COMPARISON")
        print("=" * 70)
        
        print(f"\n{'Metric':<25} {'H1 (Misplaced)':<20} {'H2 (Manhattan)':<20}")
        print("-" * 70)
        print(f"{'Nodes Explored':<25} {stats_h1['nodes_explored']:<20} {stats_h2['nodes_explored']:<20}")
        print(f"{'Solution Depth':<25} {stats_h1['solution_depth']:<20} {stats_h2['solution_depth']:<20}")
        print(f"{'Max Frontier Size':<25} {stats_h1['max_frontier_size']:<20} {stats_h2['max_frontier_size']:<20}")
        print(f"{'Time Taken (seconds)':<25} {stats_h1['time_taken']:<20.4f} {stats_h2['time_taken']:<20.4f}")
        
        # Calculate efficiency
        efficiency_h1 = stats_h1['nodes_explored'] / stats_h1['solution_depth'] if stats_h1['solution_depth'] > 0 else 0
        efficiency_h2 = stats_h2['nodes_explored'] / stats_h2['solution_depth'] if stats_h2['solution_depth'] > 0 else 0
        
        print(f"{'Efficiency (nodes/move)':<25} {efficiency_h1:<20.2f} {efficiency_h2:<20.2f}")
        
        print("\n" + "=" * 70)
        print("ANALYSIS")
        print("=" * 70)
        
        if stats_h2['nodes_explored'] < stats_h1['nodes_explored']:
            improvement = ((stats_h1['nodes_explored'] - stats_h2['nodes_explored']) / 
                          stats_h1['nodes_explored'] * 100)
            print(f"✓ Manhattan Distance (H2) explored {improvement:.1f}% fewer nodes than")
            print(f"  Misplaced Tiles (H1), making it more efficient.")
        elif stats_h1['nodes_explored'] < stats_h2['nodes_explored']:
            improvement = ((stats_h2['nodes_explored'] - stats_h1['nodes_explored']) / 
                          stats_h2['nodes_explored'] * 100)
            print(f"✓ Misplaced Tiles (H1) explored {improvement:.1f}% fewer nodes than")
            print(f"  Manhattan Distance (H2), making it more efficient.")
        else:
            print("Both heuristics explored the same number of nodes.")
        
        print("\nNote: Manhattan Distance typically performs better because it provides")
        print("more informed estimates of the actual distance to the goal state.")


def main():
    """Main function with test cases"""
    
    # Test Case 1: Easy puzzle (few moves)
    print("\n" + "█" * 70)
    print("TEST CASE 1: Easy Puzzle (4 moves)")
    print("█" * 70)
    
    initial_easy = [
        [1, 2, 3],
        [4, 0, 5],
        [7, 8, 6]
    ]
    
    goal = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]
    
    compare_heuristics(initial_easy, goal)
    
    # Test Case 2: Medium puzzle
    print("\n\n" + "█" * 70)
    print("TEST CASE 2: Medium Puzzle (8 moves)")
    print("█" * 70)
    
    initial_medium = [
        [1, 2, 3],
        [4, 5, 6],
        [0, 7, 8]
    ]
    
    compare_heuristics(initial_medium, goal)
    
    # Test Case 3: Harder puzzle
    print("\n\n" + "█" * 70)
    print("TEST CASE 3: Harder Puzzle (14 moves)")
    print("█" * 70)
    
    initial_hard = [
        [1, 2, 3],
        [0, 4, 6],
        [7, 5, 8]
    ]
    
    compare_heuristics(initial_hard, goal)
    
    # Test Case 4: Complex puzzle
    print("\n\n" + "█" * 70)
    print("TEST CASE 4: Complex Puzzle (20 moves)")
    print("█" * 70)
    
    initial_complex = [
        [7, 2, 4],
        [5, 0, 6],
        [8, 3, 1]
    ]
    
    compare_heuristics(initial_complex, goal)


if __name__ == "__main__":
    main()
