dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def travel(r,c, cnt):
    global min_v 
    visited.append((r,c))
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0<= nr <N and 0<= nc <M and not (nr,nc) in visited:
            
            
            if matrix[nr][nc] == 'W':
                if min_v > cnt:
                    min_v = cnt
                    # return cnt 
            else:
                travel(nr,nc,cnt +1)
                
    visited.pop()
    

T = int(input())

for tc in range(1, T+1):
    N, M = map(int,input().split())
    matrix = [list(input()) for _ in range(N)]
    cnt = 0
    min_v = 1000
    total = 0
    visited = []
    for r in range(N):
        for c in range(M):
            if matrix[r][c] == 'W':
                for i in range(4):
                    nr = r+dr[i]
                    nc = c+dc[i]
                if 0 <= nr < N and 0 <= nc < M
                # total += travel(r,c,cnt)
                total += min_v

    print(total) 
                