vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E', 'F'],
    'E': ['C', 'D', 'F', 'G'],
    'F': ['D', 'E', 'G'],
    'G': ['E', 'F']
}

n = len(vertices)

def print_coloring(color_array, total_colors):
    print("\nColoring Possible with", total_colors, "colors\n")
    for i in range(n):
        print("Vertex", vertices[i], "→ Color", color_array[i])
    print("\nMinimum number of colors required =", total_colors)

def is_safe(vertex_index, color, color_array):
    vertex = vertices[vertex_index]
    for neighbor in graph[vertex]:
        neighbor_index = vertices.index(neighbor)
        if color_array[neighbor_index] == color:
            return False
    return True

def solve(index, max_colors, color_array):
    if index == n:
        return True
    for color in range(1, max_colors + 1):
        if is_safe(index, color, color_array):
            color_array[index] = color
            if solve(index + 1, max_colors, color_array):
                return True
            color_array[index] = 0
    return False

def graph_coloring():
    for colors in range(1, n + 1):
        color_array = [0] * n
        if solve(0, colors, color_array):
            print_coloring(color_array, colors)
            return
    print("No coloring possible")

graph_coloring()