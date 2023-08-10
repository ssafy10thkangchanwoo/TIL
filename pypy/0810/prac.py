T = int(input())
for tc in range(1, T+1):
    def dfs(s, V):
        visited = [0]*(V+1)
        stack = []
        i = s
        visited[i] = 1

        while True:
            for j in adj[i]:
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

    V, E = map(int, input().split())

    for i in range(E):
        s, e = map(int, input().split())
        adj = [[]for _ in range(V+1)]
        adj[s].append(e)

    check1, check2 = map(int, input().split())