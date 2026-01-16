import heapq

def uniform_cost_search(graph, start, goal):
    # Priority queue: (cost, current_node, path)
    priority_queue = [(0, start, [start])]
    visited = set()

    while priority_queue:
        cost, node, path = heapq.heappop(priority_queue)

        if node in visited:
            continue

        visited.add(node)

        # Goal test
        if node == goal:
            return cost, path

        # Explore neighbors
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(
                    priority_queue,
                    (cost + weight, neighbor, path + [neighbor])
                )

    return float("inf"), []


# ---- Graph Representation ----
# Each node has (neighbor, cost)
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

start_node = 'A'
goal_node = 'D'

cost, path = uniform_cost_search(graph, start_node, goal_node)

print("Minimum Cost:", cost)
print("Optimal Path:", path)
