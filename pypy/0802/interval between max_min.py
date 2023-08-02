T = int(input())

for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int,input().split()))
    max_num = 1
    max_idx = 0
    min_num = 10
    min_idx = 0
    ## 최대/최소 구하기
    for i in range(n):
        if arr[i] < min_num:
            min_num = arr[i]
            min_idx = i
        if arr[i] >= max_num:
            max_num = arr[i]
            max_idx = i

    diff = max_idx - min_idx if max_idx > min_idx else min_idx - max_idx
    print(f'#{tc} {diff}')






