
def dfs(i, sub):
    if i == N and len(sub)==M:
        sub_set.append((sub))
        return
    else:
        for n in range(i,N+1):
            dfs(i+1, sub+[n])
            dfs(i+1, sub)


N, M = map(int,input().split())


sub_set =[]
dfs(0, [])
# sub_set = set(sub_set)
# tuple_arr = [tuple(i) for i in sub_set]

print(sub_set)