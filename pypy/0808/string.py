T = 10
for tc in range(1, T+1):
    input()
    pattern = input()
    text = input()
    M = len(pattern)
    N = len(text)

    pidx = 0
    tidx = 0
    cnt = 0

    while pidx < M and tidx < N :
        if pattern[pidx] != text[tidx]:
            tidx = tidx - pidx
            pidx = -1
        tidx += 1
        pidx += 1

        if pidx == M:
            cnt += 1
            tidx = tidx - pidx +1
            pidx = 0

    print(f'#{tc} {cnt}')







