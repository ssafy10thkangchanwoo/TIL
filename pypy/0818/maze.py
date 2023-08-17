dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(maze, start):
    q = []
    sr, sc = start
    visited = [[0]*16 for _ in range(16)]
    visited[sr][sc] = 1
    q.append((sr, sc))

    while q:
        t = q.pop(0)
        r, c = t
        if maze[r][c] == 3:
            return 1

        for i in range(4):
            nr = r + dr
            nc = c + dc
            if 0<= nr < 16 and 0<= nc < 16 and maze[nr][nc] != 3 and visited[nr][nc] ==0:
                q.append((nr,nc))
                visited[nr][nc] = visited[r][c] + 1
    else:
        return 0




def StartingPoint(maze):
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                return (i, j)


def EndPoint(maze):
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 3:
                return (i, j)



for tc in range(1, 11):
    maze = [list(map(int,input())) for _ in range(16)]
    start = StartingPoint(maze)
    End = EndPoint(maze)

    print(f'{tc} {bfs(maze, start)}')