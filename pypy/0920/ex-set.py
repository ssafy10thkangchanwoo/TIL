# 0 ~ 9
# make-set : 집합을 만들어주는 과정
parent = [i for i in range(10)] 


# find-set
def find_set(x):
    if parent[x] == x:
        return x
    
    return find_set(parent[x])

    # 경로 압축
    parent[x] = find_set(parent[x])
    return parent[x]

# union

def union(x, y):
    #  1. 이미 같은 집합인 지 체크
    x = find_set(x)
    y = find_set(y)

    # 대표자가 같으니 같은 집합이다.
    if x== y:
        return 
    
    #  2. 다른 집합이라면 , 하나의 대표자를 갖게끔 수정 
    if x < y : 
        parent[y] = x 
    else:
        parent[x] = y 

union (0, 1)
union (2, 3)

print(find_set(2))
print(find_set(3))

t_x = 0
t_y = 2
if find_set(t_x) == find_set(t_y):
    print(f'{t_x} 와 {t_y} 는 같은 집합에 속해있습니다.')
else:
    print(f'{t_x} 와 {t_y} 는 다른 집합에 속해있습니다.')