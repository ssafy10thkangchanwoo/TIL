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

V, E = map(int, input().split())

adj_list = [[] for _ in range(V+1)]

for i in range(E):
    s, e = map(int, input().split())

    # s에서 e로 가는 길이 있다.
    adj_list[s].append(e)
    # e에서 s로 가는 길ㅇ ㅣ있다.
    adj_list[e].append(s)

# 재귀를 이용해서 구현
visited = [0] * (V+1)
visited[1] = 1
# now: 현재 방문한 정점
def dfs(now):
    print(now) # 내가 어느 정점에 있는지 출력해보기
    # 현재 정점에서 방문할 수 있는 정점을 찾아 방문
    for next in adj_list[now]:
        # now에서 방문할 수 있는 next 정점
        if not visited[next]:
            visited[next] = 1
            dfs(next) # 재귀 호출

dfs(1)