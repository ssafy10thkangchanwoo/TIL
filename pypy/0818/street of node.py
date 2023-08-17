def street(arr, start, end, V):
    visited= [0]*(V+1)
    q = []
    q.append(start)
    visited[start] = 1
    while q:
        t = q.pop(0)
        for i in range(1, V+1):
            if arr[t][i] == 1:
                if visited[i] == 0:
                    q.append(i)
                    visited[i] = visited[t] +1

                if i == end:
                    return visited[i] -1
    return 0


T = int(input())
for tc in range(1, T+1):
    V, E = map(int,input().split())
    arr = [[0]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        s, e = map(int, input().split())
        arr[s][e] = 1
        arr[e][s] = 1

    start, end = map(int,input().split())
    answer = street(arr, start, end, V)
    print(f'#{tc} {answer}')








