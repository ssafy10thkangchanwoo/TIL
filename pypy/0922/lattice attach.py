def abyss(r,c,number):
    if len(number) == 7:
        result.add(number)
        return
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < 4 and 0<= nc < 4:
            abyss(nr, nc, number + matrix[nr][nc])

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


T = int(input())
for tc in range(1, T+1):
    matrix = [list((input().split())) for _ in range(4)]
    number = ''
    result = set()# number을 담는 박스
    for r in range(4):
        for c in range(4):
            abyss(r, c, matrix[r][c])

    print(f'#{tc} {len(result)}')