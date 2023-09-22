from collections import Counter
# find-set
def find_set(x):
    if parent[x] == x:
        return x

    # return find_set(parent[x])

    # 경로 압축
    parent[x] = find_set(parent[x])
    return parent[x]

# union
def union(x, y):
    # 1. 이미 같은 집합인 지 체크
    x = find_set(x)
    y = find_set(y)



    # 2. 다른 집합이라면, 같은 대표자로 수정
    if x <= y:
        parent[y] = x
    else:
        parent[x] = y


def chain_block(r,c):
    if (r, c) in visited:  # r,c를 방문했다면
        return
    visited.add((r,c))

    if matrix[r][c] == 1:
        return
    
    for pp in range(1, matrix[r][c]):
        for dr, dc in (-1, 0), (0, -1), (0, 1), (1, 0):
            dr *= pp 
            dc *= pp
            nr = dr + r 
            nc = dc + c 
            if 0<=nr<H and 0<=nc<W and matrix[nr][nc] != 0:
                union(p_matrix[r][c], p_matrix[nr][nc])
                chain_block(nr,nc)

    # for dr, dc in (-1, 0), (0, -1), (0, 1), (1, 0):
    #     nr = dr + r 
    #     nc = dc + c 
    #     if 0<=nr<H and 0<=nc<W and matrix[nr][nc] != 0:
    #         union(p_matrix[r][c], p_matrix[nr][nc])
    #         chain_block(nr,nc)


T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(H)]



    # 아래걸 N번 시행합시다. 
    for _ in range(N):

        # 부모매트릭스
        p_matrix = [[0]*W for _ in range(H)]
        parent=[i for i in range(H*W)]
        p = 0
        for r in range(H):
            for c in range(W):
                p_matrix[r][c] = p
                p+= 1

        visited = set()
        for w in range(W):
            for h in range(H): 
                if not matrix[w][h] == 0:
                    chain_block(w,h)

        for i in range (W*H):
            find_set(i)
        # print(p_matrix)
        # print(parent)+
        a = Counter(parent)
        print(a)
        print(parent.count(parent[0]))
        print(a.most_common(1))

        [(MOST, c)] = a.most_common(1)
        

        for w in range(W):
            temp_list = []
            for h in range(H):
                if p_matrix[h][w] == MOST or  matrix[h][w] == 0:
                    continue
                temp_list.append((h,w, matrix[h][w])) # 아래것일수록 늦은

            # 다시 새로운 줄을 만든다.
            for h in range(H-1, -1, -1):
                if temp_list:
                    hh, ww, po =temp_list.pop()
                    matrix[hh][ww] = po 
                else:
                    matrix[hh][ww] = 0
        print(matrix)
    cnt = 0

    for w in range(W):
        for h in range(H): 
            if not matrix[w][h] == 0:
                cnt += 1
    
    print(f'#{tc} {cnt}')



