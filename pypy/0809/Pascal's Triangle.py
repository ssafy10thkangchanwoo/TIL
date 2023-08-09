T = int(input())

for tc in range(1, T+1):
    N = int(input())
    M = N
    for n in range(N):
        tri[N][M] = tri[N-1][M-1]+tri[N-1][M]
