from collections import deque

def add_edge(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)

def bfs(start, graph, visited):
    q = deque([start])
    visited[start] = True
    while q:
        cur = q.popleft()
        print(cur, end=" ")
        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)

def dfs(node, graph, visited):
    visited[node] = True
    print(node, end=" ")
    for nxt in graph[node]:
        if not visited[nxt]:
            dfs(nxt, graph, visited)

v = 5
graph = [[] for _ in range(v)]
add_edge(graph, 0, 1)
add_edge(graph, 0, 2)
add_edge(graph, 0, 3)
add_edge(graph, 1, 3)
add_edge(graph, 2, 4)

choice = input(" 1 for BFS or 2 for DFS: ")
visited = [False]*v

match choice:
    case "1":
        bfs(0, graph, visited)
    case "2":
        dfs(0, graph, visited)
    case _:
        print("Invalid choice")
