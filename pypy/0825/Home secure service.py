def protect(r, c, ):
    for K in range(N):
        for i in (-K+1, K):
            for j in (N):
                if abs(r-i) + abs(c-j) < K:
                    earning += matrix[r-i][c-j]

            



T = int(input())
for tc in range(1, T+1):
    # N은 가로세로, M은 1가구당 지불할 금액
    N, M = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)] 
    for r in range(N):
        for c in range(N):
              
            