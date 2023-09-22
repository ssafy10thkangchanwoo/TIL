from heapq import heappush, heappop

def d(start, connect, D):
    pq = []
    heappush(pq, (0, start))
    D[start] = 0
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
for tc in range(1, T + 1):
    N, E = map(int, input().split())
    connect = [[] for _ in range(N + 1)]
    
    for _ in range(E):
        s, e, w = map(int, input().split())
        connect[s].append((e, w))
    
    D = [float('inf')] * (N + 1)
    start_node = 0  # 시작 노드. 문제에 따라 변경 가능
    d(start_node, connect, D)

    print(f"#{tc} {D[N]}")