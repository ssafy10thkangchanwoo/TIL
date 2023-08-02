T = int(input())

for tc in range(1, T+1):
    N, M = input().split()
    # N, M = map(int, input().split())
    N = int(N)
    M = int(M)
    matrix = [list(map(int, input().split())) for _ in range(N)]
    # 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    total = 0
    max_v = 0

    for i in range(N):
        for j in range(M):
            square = 0
            for d in range(4):
                nr = i + dr[d]
                nc = j + dc[d]
                if 0 <= nr < N and 0 <= nc < M:
                    matrix[nr][nc]
                    square += matrix[nr][nc]
            total = matrix[i][j] + square
            if max_v < total:
                max_v = total
            else:
                max_v
    print(f'#{tc} {max_v}')
