T = int(input())

for tc in range(1, T+1):
    N = int(input())
    r1, c1, r2, c2 = map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    avV = 0
    temp_total = 0
    cnt = 0
    for r in range(r1, r2+1):
        for c in range(c1, c2+1):
            temp_total += arr[r][c]

    avV = temp_total//((r2-r1+1)*(c2-c1+1)) # 이런건 그냥 새로운 변수 만들어라.

    total_cnt = 0
    for r in range(r1, r2+1):
        for c in range(c1, c2+1):
            cnt = arr[r][c] - avV
            if cnt <0:
                cnt = -cnt
            total_cnt += cnt


    print(f'#{tc} {total_cnt}')