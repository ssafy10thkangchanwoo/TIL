# #         A B C D E F G
# adj_m = [[0,1,1,0,0,0,0],# A
#          [1,0,0,1,1,0,0],# B
#          [1,0,0,0,1,0,0],# C
#          [0,1,0,0,0,1,0],# D
#          [0,1,1,0,0,1,0],# E
#          [0,0,0,1,1,0,1],# F
#          [0,0,0,0,0,1,0]]# G

# node = ["A", "B", "C", "D", "E", "F", "G"]
# N = 7

# def dfs(s, V):
#     visited = [0]*V
#     stack = []

#     visited[s] = 1
#     print(node[s])

#     i = s

#     while True:
#         for j in range(V):
#             if adj_m[i][j] == 1 and visited[j] == 0:
#                 stack.append(i)
#                 print(node[j])
#                 visited[j] = 1
#                 i = j
#                 break
        
#         else:
#             if stack:
#                 i = stack.pop()
#             else:
#                 break

# dfs(0,N)

# 2. 인접리스트
# adj_l[i] => i번 정점과 연결되어있는 정점의 모음(list)
# adj_l[A] = [B, C]
""""
7 8 
1 2 
1 3
2 4 
2 5 
3 7 
4 6 
5 6 
6 7 
"""

# def dfs(s, V):
#     visited = [0]*(V+1)
#     stack = []
#     i = s
#     visited [i] = 1
#     print(i)

#     while True:
#         for j in adj_l[i]:
#             if visited[j] ==0:
#                 stack.append(i)
#                 i = j
#                 visited[j] = 1
#                 print(i)
#                 break
#         else:
#             if stack:
#                 i = stack.pop()
#             else:
#                 break

# V, E = map(int, input().split()) # 정점이/ 연결된 선이 몇개있다~
# adj_l = [[] for _ in range(V+1)] 
# for i in range(E):
#     s, e = map(int, input().split())

#     adj_l[s].append(e)
#     adj_l[e].append(s)


V, E = map(int, input().split())
adj_l = [[] for _ in range(V+1)]
for i in range(E):
    s, e = map(int, input().split())
    adj_l[s].append(e)
    adj_l[e].append(s)


def dfs(s, V):
    visited = [0]*(V+1)
    stack = []
    i = s 
    visited[i] = 1
    print(i)

    while True:
        for j in adj_l[i]:
            if visited[j] == 0:
                stack.append(i)
                i = j
                visited[j] = 1
                print(i)
                break
        else:
            if stack:
                i = stack.pop()
            else:
                break


dfs(1, V)
