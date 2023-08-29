
T = int(input())
for tc in range(1, T+1): 
    N, M = map(int,input().split()) # N 크기, M 수익
    matrix = [list(map(int,input().split())) for _ in range(N)]
    home = []
    for r in range(N):
        for c in range(N):
            if matrix[r][c] == 1:
                home.append((r,c))


    max_num_all = 0
    for r in range(N):
        
        for c in range(N):
            house = [0]*2*N
            cnt = 0
            max_num = 0
            for K in range(1, 2*N):
                for rh, ch in home:
                    
                    if abs(r-rh) + abs(c-ch) <= K-1:
                        cnt += 1
                        house[K] = cnt

            for K in range(1,2*N):
                
                cost = K*K + (K-1)*(K+1)
                if house[K]*M-cost >= 0:
                    max_num = house[K]
                if max_num > max_num_all:
                    max_num_all = max_num
    print(f'#{tc} {max_num_all}')