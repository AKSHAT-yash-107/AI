import heapq
import numpy as np
import matplotlib.pyplot as plt

def heuristic(a, b, type="manhattan"):
    if type == "manhattan":
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    elif type == "euclidean":
        return np.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
    return 0

def a_star(grid, start, goal, h_type="manhattan"):
    rows, cols = grid.shape
    neighbors = [(0,1), (0,-1), (1,0), (-1,0)]
    if h_type == "euclidean":
        neighbors += [(1,1), (1,-1), (-1,1), (-1,-1)] 

    close_set = set()
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal, h_type)}
    oheap = []

    heapq.heappush(oheap, (f_score[start], start))
 
    while oheap:
        current = heapq.heappop(oheap)[1]

        if current == goal:
            data = []
            while current in came_from:
                data.append(current)
                current = came_from[current]
            return data[::-1] 

        close_set.add(current)
        for i, j in neighbors:
            neighbor = current[0] + i, current[1] + j
            
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols:
                if grid[neighbor[0]][neighbor[1]] == 1: 
                    continue
            else:
                continue

            tentative_g_score = g_score[current] + heuristic(current, neighbor, h_type)
            
            if neighbor in close_set and tentative_g_score >= g_score.get(neighbor, float('inf')):
                continue
                
            if tentative_g_score < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal, h_type)
                heapq.heappush(oheap, (f_score[neighbor], neighbor))
                
    return False

grid = np.zeros((10, 10))
grid[3:7, 5] = 1 
start, goal = (0, 0), (9, 9)

path = a_star(grid, start, goal, h_type="manhattan")

if path:
    px, py = zip(*path)
    plt.imshow(grid, cmap='Greys')
    plt.plot(py, px, marker='o', color='red')
    plt.scatter([start[1], goal[1]], [start[0], goal[0]], color='green', s=100)
    plt.title("A* Search Pathfinding")
    plt.show()