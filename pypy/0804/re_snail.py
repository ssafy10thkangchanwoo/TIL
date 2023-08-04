T = int(input())

# d = 0 오른쪽
# d = 1 아래
# d = 2 왼쪽
# d = 3 위쪽

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
for tc in range(1, T + 1):
    N = int(input())

    # 달팽이집을 0으로 다 채워서 N*N만큼 만들어주기

    snail = [[0] * N for _ in range(N)]
    r = 0
    c = 0
    d = 0
    for n in range(1, N + 1):
        snail[r][c] = n

        nr = r + dr[d]
        nc = c + dc[d]

        if 0 <= nr < N and 0 <= nc < N and snail[nr][nc] == 0:
            r = nr
            c = nc

        else:
            d += 1

    print(f'#{tc} {snail}')
