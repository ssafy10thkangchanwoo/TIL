def check(nr,nc):
    return 0<=nr<N and 0<=nc<N

def travel(r,c,total):
    if (r,c) == (N-1, N-1):
        min_v = min(total, min_v)




    # for dr, dc in ((1,0),(0,1)):
    #     nr = r+dr
    #     nc = c+dc
    #     if check(nr,nc):
    #         total+= arr[nr][nc]
    #         travel(nr,nc,total)
    #         total-= arr[nr][nc]

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    min_v = 9990
    