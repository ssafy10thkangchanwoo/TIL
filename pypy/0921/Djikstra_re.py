from heapq import heappop, heappush

INF = 1000000000 # 무한대 초기화 용

def dijikstra(s):
    q = []
    heappush(q, (0,s)) # (가중치, 정점 번호)
    D[s] = 0 # 시작정점 비용은 0

    while q:
        print(D)
        # w 가중치, v 정점번호, 최소거리문제에서는 가중치가 거리
        w, v = heappop(q)

        # 방금 꺼내온 v번 노드까지의 가중치 w가 
        # 이전에 계산해 놓은 v번 까지의 최소 거리보다 크면 계산할 필요 x 
        # D[t]는 처음에 무한대로 초기화 해 놨으니 계산한 적이 있는지 체크도 가능
        if D[v] < w:
            continue 
        
        # v와 연결된 정점을 탐색
        # u : v와 연결된 정점 번호
        # uw : v에서 u까지의 가중치
        for u, uw in adjl[v]: 
            cost = D[v] + uw  # v까지의 가중치 + v에서 u까지의 가중치 = v에서 u까지 가는 가중치
            if cost<D[u]: # 방금 계산한 거리가 이전에 계산한 거리보다 작으면
                D[u] = cost
                heappush(q, (cost,u)) # 최단거리가 갱신된 경우에만 큐에 삽입
    


V , E = map(int, input().split())
adjl = [[] for _ in range(V)]
    
for i in range(E):
    # s: 시작 정점, e : 도착, w, 가중치
    s, e, w = map(int, input().split())
    adjl[s].append((e,w))

# D[i] = 시작지점 a에서 i까지 가는데 걸리는 최소 비용

D = [INF] * V 