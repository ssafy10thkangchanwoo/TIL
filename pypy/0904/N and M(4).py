
def dfs(i,sub):
    if i == M:
        if len(sub) == 2:
            ans.append(sub)
        return

    else:
        for n in range(1, N+1):
            dfs(i+1, sub+[n])

N, M = map(int,input().split())

ans = []
dfs(0,[])
print(ans)

