
def travel(c,total):
    if (r,c) == (N-1, N-1):
        min_v = min(total, min_v)
    




   

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    min_v = 9990
    visited = []
    c = 1 