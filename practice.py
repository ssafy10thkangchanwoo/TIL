T = 10
for tc in range(1, T+1):
    pattern = input()
    text = input()
    M = len(pattern)
    N = len(text)

    pidx = 0
    tidx = 0
    cnt = 0

    while tidx < N: # tidx가 N보다 작은 동안 계속 검사
        if pattern[pidx] != text[tidx]:
            tidx = tidx - pidx + 1
            pidx = 0 # 패턴의 시작부터 다시 비교
        else:
            pidx += 1
            tidx += 1

        if pidx == M:
            cnt += 1
            tidx = tidx - pidx + 1 # 패턴 발견된 위치의 다음 인덱스로 이동
            pidx = 0 # 패턴의 시작부터 다시 비교

    print(f'#{tc} {cnt}')