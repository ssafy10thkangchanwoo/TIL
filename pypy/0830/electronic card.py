def travel(s,cost,visited):
    global min_sum
    if sum(visited) == N:
        min_sum = min(cost,min_sum)
        return min_sum
    for i in range(1,N+1):
        # if not i in visited:
        if visited[i] ==0 and i != s:
            cost += e[s][i]
            visited[i] = 1
            travel(i,cost, visited)
            cost -= e[s][i]
            visited[i] = 0

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    e = [list(map(int,input().split())) for _ in range(N)]
    visited = [0]*(N+1)
    (r,c) = (1,1)
    cost = 0
    visited[1] = 1
    min_sum = 9999
    answer = travel(c,cost,visited)
    print(f'#{tc} {answer}')