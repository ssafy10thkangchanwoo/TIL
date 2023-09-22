from heapq import heappush, heappop

def d(s):
    pq = []
    heappush(pq, (0,s)) # 첫번쨰가 가중치/ 두번째가 현위치
    D[s] = 0 
    while pq:
        w,now = heappop(pq)
        # 대충 지금 값보다 다음단계 값이 크다는 소리
        # w는 지금까지 가중치의 값 
        # 지금까지의 가중치값이 현위치까지 오는데 걸리는 최소비용보다 크면 continue
        if w > D[now]:
            continue 

        # 지금까지가 더 비용이 저렴하면 업데이트해야지.
        # connect[now] 현위치에서 새로 갈 곳을 검사해봐서
        # 시작점부터 새로 갈 곳의 최소비용 vs 시작점부터 현재위치까지의 최소비용+ 현재위치에서 새로 갈 곳의 비용
        # 시작점부터 새로갈곳까지의 비용이 여전히 더 저렴하다면야 놔두고 
        # 아니라면 업데이트하자.

        for ne, nw in connect[now]:
            if D[ne] <= w+ nw :
                continue 
            
            D[ne] = w + nw
            heappush(pq,(nw+w,ne))

        


T = int(input())
for tc in range(1, T+1):
    N, E = map(int,input().split())
    connect = [[] for _ in range(N+1)]


    # for _ in range(E):
    #     road_list= list(map(int,input().split()))
    #     roads.append(road_list)
    
    # for s, e, w in roads:
    #     connect[s].append(e,w)
    
    # 위 두문단의 코드를 아래의 코드로 표현가능
    for _ in range(E):
        s, e, w = map(int,input().split())
        connect[s].append((e,w)) # append는 하나의 인자만 취급가능
        # connect[s].append((e,w)) : s에서 e로 갈 수 있음. 가중치는 w임
    
    D = [99999]*(N+1)  # D 시작점(0)에서 특정 정점[인덱스]까지 가는데 걸리는 최소 비용
    s = 0
    d(s)
    print(f"#{tc} {D[N]}")