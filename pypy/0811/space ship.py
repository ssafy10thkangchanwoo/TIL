T = int(input())
for tc in range(1, T+1):
    c, w = map(int, input().split())
    land = [list(map(int,input().split())) for _ in range(c)]
    dr = [-1, 1, 0, 0, -1, -1, 1, 1]
    dc = [0, 0, -1, 1, -1, 1, -1, 1]
    result = 0

    for i in range(0, c):
        for j in range(0, w):
            counts = 0
            for d in range(8):
                n_i = i+dc[d]
                n_j = j+dr[d]
                if 0<= n_i < c and 0<= n_j < w:
                    if land[i][j] > land[n_i][n_j]:
                        counts += 1

            if counts >= 4:
                result += 1

    print(f'#{tc} {result}')