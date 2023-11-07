from collections import deque 
# 위층아래층 상하좌우
dr = [0,0,-1, 1, 0, 0]

dc = [0,0,0, 0, -1, 1]

dh = [-1,1,0,0,0,0]
def bfs(sp,matrix):
    q = deque([])
    for (h,i,j) in sp:
        q.append((h,i,j))

    while q:
        ch, ci, cj = q.popleft()                   
        for 

def check(matrix, H, W):
    answer = 0
    for h in range(1, H+1):
        for i in range(1, H+1):
            for j in range(1, W+1):
                if matrix[i][j] == 0:  
                    return -1
                answer = max(matrix[i][j], answer)
        return answer - 1 

# 가로세로높이
M, N, H = list(map(int,input().split()))

matrix = [[-1]+list(map(int,input().split()))+[-1] for _ in range(H)]

matrix = [[-1]*(M+2)] + matrix + [[-1]*(M+2)]

sp = []
for h in range(1, H+1):
    for i in range(1, N+1):
        for j in range(1, M+1):
            if matrix[h][i][j] == 1:
                sp.append((h,i,j))


bfs(sp,matrix)

# answer = check(matrix, H, W) 
check()
# print(answer)