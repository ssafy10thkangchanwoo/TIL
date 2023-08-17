def BFS(G, v):
    visited = [0] * (n+1)
    queue = []
    queue.append(v)
    while queue:
        t = queue.pop(0)
        