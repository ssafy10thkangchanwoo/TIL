T = int(input())

def find(x):
    if p[x] == x:
        return x 
    else:
        p[x] = find(p[x])
        return p[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        p[y] = x 
    elif x == y:
        return 
    else:
        p[x] = y 

for tc in range(1, T+1):
    # 0번부터 V번까지 노드래.
    V, E = map(int,input().split())
    p = [i for i in range(0, V+1)]
    edge = []
    for _ in range(E):
        s, e, w = map(int,input().split()) 
        edge.append([s,e,w])
    
    edge.sort(key = lambda x: x[2])


    total = 0
    cnt = 0
    for s, e, w in edge:
        if find(s) != find(e):
            union(s, e)
            cnt += 1
            total += w 
        
        if cnt == V: # V-1가 아니라 V라네
            break
    print(f'#{tc} {total}')



