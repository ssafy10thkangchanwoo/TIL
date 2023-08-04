T = int(input())

for tc in range(1, T+1):
    N, M = input().split()
    # N, M = map(int, input().split())
    N = int(N)
    M = int(M)
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    total = 0
    max_v = 0



for i in range(N):
    for j in range(M):
        cnt = arr[i][j]
        for k in range(4):
            ni, nj = i+dk[k], j[dj]
            # 가장자리 벗어나는지에 대한 범위 조사
            if 0<= ni < N and 0 <= nj < M:
                cnt += arr[ni][nj]
                
        if max_v < cnt:
            max_v = cnt