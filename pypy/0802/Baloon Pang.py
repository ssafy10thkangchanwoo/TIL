T = int(input())

for tc in range(1, T+1):
    N, M = input().split()
    N = int(N)
    M = int(M)
    matrix = [list(map(int, input().split())) for _ in range(N)]


    total = 0
    max_v = 0

    for i in range(N):
        for j in range(M):
            square = 0
            middle = matrix[i][j]
            # 상하좌우
            for m in range(1, middle+1):
                dr = [m, -m, 0, 0]
                dc = [0, 0, -m, m]

                for d in range(4):
                    nr = i + dr[d]
                    nc = j + dc[d]
                    if 0 <= nr < N and 0 <= nc < M:
                        matrix[nr][nc]
                        square += matrix[nr][nc]
                total = matrix[i][j] + square
                if max_v < total:
                    max_v = total
    print(f'#{tc} {max_v}')
