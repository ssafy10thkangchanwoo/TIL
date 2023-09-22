def bfs(s):
    q = [s]
    visited = [0]*101
    visited[s] = 1

    # 최대숫자, 최대 깊이
    max_n = 0
    max_d = 1
    while q :
        now =  q.pop(0)

        # 갈 수 있는 지점 다 봐라
        for to in graph[now]:
            if visited[to]:
                continue

            # 기존 방문보다 한 번 더 갔다. # 깊이를 추가하는 것이네요
            visited[to] = visited[now] + 1

            # 한단계 깊은 곳으로 가거나, 깊이는 같은데 숫자가 더 크다면 max값 갱신
            if max_d < visited[to] or (max_d == visited[to]) and max_n < to:
                max_d = visited[to]
                max_n = to
            q.append(to)
    return max_n

for tc in range(1, 11):
    n, start = map(int,input().split())
    # 임시로 전체 입력을 받음
    input_graph = list(map(int,input().split()))
    graph = [[] for _ in range(101)]
    for i in range(0, n, 2):
        f = input_graph[i]
        t = input_graph[i+1]
        graph[f].append(t)

    answer = bfs(start)
    print(f'#{tc} {answer}')

    # bfs(start)
    # print(max_n)

