from heapq import heappush, heappop

def d(s, connect, D):
    pq = [(0, s)]
    D[s] = 0
    while pq:
        w, now = heappop(pq)
        if w > D[now]:
            continue

        for ne, nw in connect[now]:
            if D[ne] <= w + nw:
                continue
            
            D[ne] = w + nw
            heappush(pq, (D[ne], ne))

T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    connect = [[] for _ in range(N+1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        connect[s].append((e, w))
    
    D = [float('inf')] * (N + 1)
    d(0, connect, D)
    print(f"Case #{tc}: {D[-1]}")
