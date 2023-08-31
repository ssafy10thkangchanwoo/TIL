T = int(input())
for tc in range(1, T+1):
    N = int(input())
    time = []
    for _ in range(N):
        time.append(list(map(int,input().split())))
    time.sort(key=lambda x:x[1]) 
    # print(time)
    time = [[0,0]] + time # 0,0넣고
    S =[] # 이건 뭐꼬
    j = 0 
    for i in range(1, N+1): # 1부터 N-1까지
        if time[i][0] >= time[j][1]:# si>=fj # 
            S.append(i)
            j = i
    print(f'#{tc} {len(S)}')