def dfs(i, visited, cnt):
    global min_c

    if cnt > min_c:
        return
    if not connect[i]:
        min_c = min(min_c, cnt)
        return
    else:
        for j in connect[i]:
            visited[j] = 1
            dfs(j, visited, cnt+1)
            visited[j] = 0


T = int(input())
for tc in range(1, T+1):
    charge = list(map(int,input().split()))
    bus_stop = charge.pop(0)
    connect = [[] for _ in range(bus_stop+1)]
    visited = [0]*(bus_stop+1)
    cnt = 0
    min_c = 9999
    for i in range(bus_stop, 0, -1):
        for j in range(1,i):
            if j+charge[j-1] >= i:
                connect[i].append(j)
    dfs(bus_stop, visited, cnt)
    print(f'#{tc} {min_c-1}')
    
    
    
