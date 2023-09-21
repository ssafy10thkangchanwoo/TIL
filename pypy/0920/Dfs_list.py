graph = [
    [1, 3],
    [0, 2, 3, 4],
    [1],
    [0, 1, 4],
    [1, 3],
]

visited = [0]*5
path = [] # 방문 순서 기록

def dfs(now):
    visited[now]= 1 # 현재 지점 방문 표시
    print(now, end = ' ')
    # 인접한 노드들을 방문
    for next in range(len(graph[now])):
        if graph[now][next]:
            continue 

        if visited[next]:
            continue 

        dfs(next)

print('dfs 재귀 =', end = ' ')
dfs(0)