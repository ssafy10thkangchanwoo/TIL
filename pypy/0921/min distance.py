from heapq import heappush, heappop

def d(s):
    pq = []
    heappush(pq, (0,0))
    D[0] = 0 
    while pq:
        now, w = heappop(pq)
        # 대충 지금 값보다 다음단계 값이 크다는 소리
        # w는 지금까지 가중치의 값 
        if w >= D[now]:
            continue 

        for ne, nw in connect[now]:
            if D[ne] < w+ nw :
                continue 
            
            heappush(pq,(ne,nw))

        



T = int(input())
for tc in range(1, T+1):
    N, E = map(int,input().split())
    roads = []
    connect = [[] for _ in range(N)]
    for _ in range(E):
        road_list= list(map(int,input().split()))
        roads.append(road_list)
    
    for s, e, w in roads:
        connect[s].append(e,w)
    
    D = [99999]*N 