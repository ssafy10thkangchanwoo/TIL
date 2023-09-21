graph = [
    [1, 3],
    [0, 2, 3, 4],
    [1],
    [0, 1, 4],
    [1, 3],
]

def bfs(n):
    visited = [0]*5 
    que = [ n ]
    visited[n] = 1

    while que:
        now = que.pop(0)
        path.append(now)
        for i in graph[now]:
            if not visited[i]:
                visited[i] = 1 
                que.append(i)






path=[]
bfs(0)

print(path)