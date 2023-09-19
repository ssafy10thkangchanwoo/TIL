import copy
def connecting(co, r, c, matrix, cnt):
    global min_connect, core, N
    if cnt >= min_connect:  # 최적화: 현재까지의 최소 연결 길이보다 크면 탐색 종료
        return
    if co == len(core):  # 모든 코어를 탐색했는지의 여부도 종료 조건으로 추가
        min_connect = min(cnt, min_connect)
        return

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    for i in range(4):
        tmp_matrix = copy.deepcopy(matrix)
        nx, ny = r + dx[i], c + dy[i]
        
        # 범위 내에 있고, matrix 값이 0인지 확인 (즉, 연결 가능한지)
        while 0 <= nx < N and 0 <= ny < N and tmp_matrix[nx][ny] == 0:
            tmp_matrix[nx][ny] = 2
            nx += dx[i]
            ny += dy[i]
        
        # 연결했을 때 끝까지 도달한 경우
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            if co+1 < len(core):
                nr, nc = core[co+1]
                new_cnt = cnt + max(abs(nx-r)-1, abs(ny-c)-1)
                connecting(co+1, nr, nc, tmp_matrix, new_cnt)

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

core = []
co_max, co, cnt = 0, 0, 0
min_connect = 9999

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            core.append((i, j))
            co_max += 1

r, c = core[0]
connecting(co, r, c, matrix, cnt)
print(min_connect)