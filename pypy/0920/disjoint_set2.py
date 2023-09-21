p = [0]*9
rank = [0]*9

# 1. 집합초기화

def make_set(x):
    p[x] = x
    # 처음 트리의 깊이는 0
    rank[x] = 0

# 2. 대표를 찾는 연산

def find_set(x) : 
    # 경로압축 
    if x != p[x]:
        p[x] = find_set(p[x])

    return p[x] 

def find_set2(x):
    while x != p[x]:
        x = p[x]
    return x 

# 3. 두 집합을 합치는 연산
def union(x, y):
    # x집합의 대표와 y집합의 대표를 찾기
    x = find_set(x)
    y = find_set(y) 
    # x집합과 y집합을 합칠 때 트리의 깊이가 더 큰쪽이 대표가 된다.
    # x집합의 깊이가 y집합의 깊이보다 크니까 대표를 x로 
    if rank[x] > rank[y]:
        p[y] = x
    else:
        # 그게 아니면 일단 대표를 y로
        p[x] = y 
        # 만약 두 집합의 깊이가 같은 경우 깊이를 + 1 증가
        if rank[x] == rank[y]:
            rank[y] += 1


for i in range(1, 9):
    make_set(i) 

rank[1] = 1
rank[2],rank[4] = 2, 2
rank[3],rank[5] = 3, 3
rank[6],rank[7],rank[8] = 4, 4, 4

union(1, 2)
union(2, 3)
union(1, 4)
union(2, 5)
union(5, 6)
union(5, 7)
union(5, 8) # disjoint_set 추가된 것
print(p)
print(find_set(1)) # findset을 한번이라도 해야 경로압축이 일어난다.
print(p)