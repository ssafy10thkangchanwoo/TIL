

def find_set(x):
    while x != p[x]:
        x = p[x]

    return x 

def union(x,y):
    x = find_set(x)
    y = find_set(y)

    if x < y:
        p[y] = x
    else:
        p[x] = y

V, E = map(int, input().split())
edge = []

for _ in range(E):
    s, e, w = map(int,input().split())
    edge.append((w, s, e)) # 리스트 넣을 때 가중치를 맨 앞으로
    
edge.sort() # 맨 앞 원소(가중치) 기준으로 오름차순 정렬

cnt = 0 
total = 0

# 정렬된 리스트를 순회하면서 가중치가 작은 간선의 정보부터 확인 
for w, s, e in edge:
    # s 정점이 속한 집합의 대표와 e 정점이 속한 대표가 같지 않아야 한다.
    # 대표가 같으면 같은 집합에 속해있다는 의미 => 싸이클이 생겨버린다.
    if find_set(s) != find_set(e):
        cnt += 1 
        union(s, e)
        total += w 
        # MST 구성이 끝나면 종료
        if cnt ==V:
            break