T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]

    i = 0
    j = 0
    ans = 0
    # for i in range(N-3):
    #     cnt = 0
    #     for j in range(N-3):
            # if matrix[N-3] + matrix[N-2] + matrix[N-1] == K:
            #     cnt += 1
    for i in range(N):
        cnt = 0
        for j in range(N):
            if matrix[i][j] == 1:
                cnt += 1
            if j==(N-1) or matrix[i][j] == 0:
                if cnt == K:
                    ans += 1
        
    for i in range(N):
        cnt = 0
        for j in range(N):
            if matrix[j][i] == 1:
                cnt += 1
            if j==(N-1) or matrix[j][i] == 0:
                if cnt == K:
                    ans += 1      

    print(ans)
