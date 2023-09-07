N = int(input())
M = int(input()) # 부분집합의 원소 개수
s = [n for n in range(1,N+1)]
sub_set = []

for i in range(1<<N):
    temp = []
    for j in range(N):
        if i&(j<<1):
            git@lab.ssafy.com:s10/python/web.git