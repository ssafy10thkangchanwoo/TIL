def dfs(i, sub):
    if i == N:
        route.append(sub)
        return
    else:
        for n in range(1, N+1):  
            if n not in visited:
                visited.append(n)
                dfs(i+1, sub+[n])



T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    sub = []
    visited = []
    route = []
    dfs(0, sub)
    print(route)