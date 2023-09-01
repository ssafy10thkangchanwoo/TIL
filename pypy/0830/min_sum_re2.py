T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    
    # (r,c)까지 오는데 최소 합은 위 또는 왼쪽 둘중에 작은거 선택
    # (r,c-1) => (r,c) or (r-1,c) ->(r,c)

    # 중간위치(r,c)까지의 합을 다시 게산하지 않도록 저장
    arr_sum = [[0]* N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            # r,c 위치로 위에서 오던가 왼쪽에서 오던가
            if r-1>=0 and c-1>=0:
                arr_sum[r][c] = min(arr_sum[r-1][c], arr_sum[r][c-1]) + arr[r][c]
            # 위쪽에서만 올 수 있다.
            elif r-1>=0 and c-1 <0:
                arr_sum[r][c] = arr[r-1][c] + arr[r][c]
            # 왼쪽에서만 올 수 잇다.
            elif r-1 < 0 and c-1>=0:
                arr_sum[r][c] = arr_sum[r][c-1] + arr[r][c]
            # 왼쪽도 없고 위쪽도 없는 시작점
            elif r-1 <0 and c-1<0:
                arr_sum[r][c] = arr[r][c]
    
    #반복이 다 끝나고 나서 n-1

