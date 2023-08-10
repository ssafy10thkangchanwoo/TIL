'''
V E 
v1 w1 v2 w2
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
''' 
def dfs(n, V, adj_m):
    stack = []# stack 생성
    visited = []*(V+1)# visited 생성
    visited[n] = 1    # 시작점 방문 표시
    print(n)# do[n]
    while True:
        for w in range(1, V)# 현재정점 n에 인접하고 미방문 w 찾기
            if adj_m[n][w] == 1 and visited[w] == 0:
                stack.append(n)#push(v), v = w
                n = w
                print(n) #do(w)
                visited[n] = 1 # #w방문표시
                break # for w, n에 인접인 w찾는경우(for에대한)

        else:
            if stack: # 스택에 지나온 정점이 남아있으면
               n = stack.pop() # pop해서 다시 다른 w 찾을 n준비
            else: #스택이 비어있으면
                break#(while True)탐색 끝

V, E = map(int, input().split())
# 1번부터  V개의 정점, E개의 간선

arr = list(map(int, input().split()))
adj_m = [[0]*(V+1) for _ in range(V+1)]

for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adj_m[v1][v2] = 1
    adj_m[v2][v1] = 1

print()

dfs(1, V, adj_m)