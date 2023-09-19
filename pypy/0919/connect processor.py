def connecting(co, r, c, matrix, cnt):
    global min_connect
    if co == max(co, co_max):
        min_connect = min(cnt, min_connect)
        return 
    for i in range(4):
        if i == 0: # 상
            if sum(matrix[:r]) == 0:
                matrix[:r] = 2
                (nr,nc) =core[i+1]
                connecting(co+1, nr, nc, matrix, cnt+(r-1))
                matrix[:r] = 0
                co += 1
        if i == 1: # 하
            if sum(matrix[r+1:]) == 0:
                matrix[r+1:] = 2
                (nr,nc) =core[i+1]
                connecting(co+1, nr, nc, matrix, cnt+(N-r))
                matrix[r+1:] = 0
                co += 1
        if i == 2: # 좌
           if sum(matrix[r][:c]) == 0:
                matrix[r][:c] = 2
                (nr,nc) =core[i+1]
                connecting(co+1, nr, nc, matrix, cnt+(c-1))
                matrix[r][:c] = 0
                co += 1
        if i == 3: # 우
           if sum(matrix[r][c+1:]) == 0:
                matrix[r][c+1:] = 2
                (nr,nc) =core[i+1]
                connecting(co+1, nr, nc, matrix, cnt+(N-c))
                matrix[r][c+1:] = 0
                co += 1
        (nr,nc) =core[i+1]
        connecting(co, r, c, matrix, cnt+(c-1))
N = int(input())

matrix = [list(map(int,input().split())) for _ in range(N)]

core = []
co_max = 0
co = 0
cnt = 0
min_connect = 9999
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            core.append((i, j))
r, c = core[0]
connecting(co, r, c, matrix, cnt)
print(min_connect)





