T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    min_idx = 0 # 최솟값의 인덱스
    max_idx = 0
    for i in range(1, N+1):
        if arr[min_idx] > arr[i]:
            min_idx = i
        if arr[max_idx] < arr[i]:
            min_idx = i
        print(min_idx)
    ans = max_idx - min_idx
    print(ans)
