def fac(i, visited, cost):
    global min_c
    if i == N:
        min_c = min(min_c, cost)
        return
    else:
        for j in range(N):
            if not visited[j]:
                new_cost = cost + matrix[i][j]
                if new_cost < min_c: 
                    visited[j] = True
                    fac(i+1, visited, new_cost)
                    visited[j] = False

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    min_c = sum(matrix)
    visited = [False] * N  
    fac(0, visited, 0)
    print(f'#{tc} {min_c}')