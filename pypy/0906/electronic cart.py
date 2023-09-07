def dfs(i, sub):
    if i == N:
        if sub and sub[0] == 1:  # sub가 비어 있지 않고, 첫 번째 원소가 1인 경우만 추가
            ans.append(sub[:])  # sub의 복사본을 추가
        return
    else:
        for n in range(1, N + 1):
            if n not in visited:
                visited.append(n)
                dfs(i + 1, sub + [n])
                visited.pop()


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    sub = []
    visited = []
    ans = []
    dfs(0, sub)
    max_v = 0
    for s in ans:
        total = 0
        for i in range(N - 1):
            total += matrix[s[i] - 1][s[i + 1] - 1]  # 인덱스는 0부터 시작하므로 -1
        all_total = total + matrix[s[N - 1] - 1][s[0] - 1]  # 마지막과 첫 번째를 연결, 인덱스는 0부터 시작하므로 -1
        max_v = max(max_v, all_total)
    print(max_v)  # 최대값 출력 (ans가 아님)