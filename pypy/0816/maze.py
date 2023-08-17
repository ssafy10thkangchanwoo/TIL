T = int(input())
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]
    answer = 0
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 2:
                in_r = r, in_c = c
            elif arr[r][c] == 3:
                out_r = r, out_c = c

    for d in range(4):
        r = in_r, c = in_c
        nr = r + dr[d]
        nc = c + dc[d]
        if nr == out_r and nc == out_c:
            answer = 1
        while 0 <= nr <N and 0 <= nc <N and arr[nr][nc] != 1:
            r = nr
            c = nc
        else:
            break





