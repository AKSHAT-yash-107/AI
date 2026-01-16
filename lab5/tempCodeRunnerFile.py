
choice = input(" 1 for BFS or 2 for DFS: ")
visited = [False]*v

match choice:
    case "1":
        bfs(0, graph, visited)
    case "2":
        dfs(0, graph, visited)
    case _:
        print("Invalid choice")
