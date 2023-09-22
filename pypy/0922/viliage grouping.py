T = int(input())

# def find(x):
#     if p[x] == x:
#         return x 
#     return find(p[x])
   
    # p[x] = find(p[x])
    # return p[x]
def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x] 

def union(x, y):
    x = find(x)
    y = find(y) 

    if x<=y:
        p[y] = x 
    else:
        p[x] = y 



for tc in range(1, T+1):
    N, M = map(int,input().split())
    # connection = [[] for _ in range(N+1)]
    p = [i for i in range(N+1)]
    for _ in range(M):
        p1, p2 = map(int,input().split())
        union(p1, p2)

    # 위에 findset된거 아님?
    # for i in range (N+1):
    #     find(i)
    # find(6)
    print(p)
    # print(f'#{tc} {'ii'}')

    du_X = set(p)
    print(f'#{tc} {len(du_X)-1}')

    
    

    