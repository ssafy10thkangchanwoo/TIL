T = int(input())
for tc in range(1, T+1):
    N, K = map(int,input().split())
    arr = list(map(int,input().split()))
    temp = [0]*len(arr)
    sub = []
    cnt = 0 # 합이 K가 되는 수
    for i in range(1, 1<<len(arr)):
        s = 0 # 부분집합의 합
        for j in range(len(arr)): # j번 비트
            if i&(1<<j): # i의 j번 비트 검사
                s += arr[j] # 0이 아니면 j번 원소가 부분집합에 포함됨
                temp[j] = 1
        if s == K:
            cnt += 1
    print(f'#{tc} {cnt}')
        