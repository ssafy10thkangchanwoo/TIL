T = int(input())
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def starting_point(maze):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j

def bfs(sr, sc, N):
    visited = [[0]*N for _ in range(N)]
    q = []
    q.append((sr,sc))
    visited[sr][sc] = 1
    while q:
        r, c = q.pop(0)
        if maze[r][c] == 3:
            return visited[r][c] -2

        for i in range(4):
            nr = r+dr[i]
            nc = c+dc[i]
            if 0 <= nr < N and 0 <= nc < N and maze[nr][nc] != 1 and visited[nr][nc] == 0:
                q.append((nr, nc))
                visited[nr][nc] = visited[r][c]+1
    return 0


for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int,input())) for _ in range(N)]
    sr, sc = starting_point(maze)
    print(f'#{tc} {bfs(sr, sc, N)}')




