T = int(input())
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
ddr = [-1, -1, 1, 1]
ddc = [-1, 1, -1, 1]

for tc in range(1, T+1):
    N, M = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    max_v = 0
    for r in range(N):
        for c in range(N):
            area_kill = matrix[r][c]
            for d in range(4):
                for s in range(1, M):
                    nr = r+ dr[d]*s
                    nc = c+ dc[d]*s
                    if 0 <= nr < N and 0 <= nc < N:
                        area_kill += matrix[nr][nc]
            if area_kill > max_v:
                max_v = area_kill

            area_kill_d = matrix[r][c]
            for d in range(4):
                for s in range(1, M):
                    nr = r+ ddr[d]*s
                    nc = c+ ddc[d]*s
                    if 0 <= nr < N and 0 <= nc < N:
                        area_kill_d += matrix[nr][nc]
            if area_kill_d > max_v:
                max_v = area_kill_d
    print(f'#{tc} {max_v}')

                    