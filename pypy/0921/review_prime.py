# 프림이 뭔가?
 # 갈 수 있는 정점을 탐색하는 기법, 최소값만 선택하고 싸이클 발생시 그 다음 최소값을 탐색한다.
#싸이클 발생여부는 union으로 알 수 있겠다.


# 쿠르스칼인듯
def find_set(x):
    if p[x] == x:
        return x 
    else:
        p[x] = find_set(p[x])

def union_set(x, y):
    x = find_set(x)
    y = find_set(y)
    if x < y : 
        p[y] = x

    elif x == y :
        return # 싸이클 발생 , 같은 집합
    else:
        p[x] = y 
    
V , E = map(int, input().split())
p = [0]*V 
edge = []
for _ in range(E):
    f, t, w = map(int,input().split())
    edge.append([f, t, w])
edge.sort(key=lambda x: x[2])

    # edge에서 하나씩 작은값을 빼가면서 서로소인지 확인하고 아니면 결합시킴
cnt = 0
total_w = 0
for f, t, w in edge: 
    if find_set(f) != find_set(t):
        total_w += w 
        cnt += 1
        union_set(f, t)
        if cnt ==V:
            break 
