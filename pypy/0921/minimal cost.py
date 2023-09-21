import heapq


def d(r, c):
    pq = []
    # 출발점 초기화
    heapq.heappush(pq, (0, r, c))
    # 갈곳을 pq에 저장, 이때까지의 비용과 위치 저장
    distance[r][c] = 0
    # 이 시점에서 비용은 0이오

    while pq: # 갈곳이 있다면 진행하시게
        dist, r, c= heapq.heappop(pq)
        # 갈곳에 대한 정보 비용, 위치

        # 지금까지 방문한 비용이 지금 위치의 최소이동거리보다 크다면 out
        if distance[r][c] < dist:
            continue
    
        # 아니라면 다음 이동할 곳의 후보군을 고르자 (아래, 오른쪽)
        for (dr, dc) in (0, 1), (1, 0), (-1,0), (0, -1):
            nr = r + dr 
            nc = c + dc 
            b = 0
            if 0<= nr <N and 0<= nc < N:
                # 다음으로 갈 곳이 더 고지대라면 비용청구
                if matrix[r][c] < matrix[nr][nc]:
                    b = matrix[nr][nc]-matrix[r][c]

                # 다음으로 가기 위한 비용
                new_cost = dist + b +1 

                # 다음 행선지의 비용보다 지금이 더 크면 out
                if distance[nr][nc] <= new_cost:
                    continue



                if distance[nr][nc] <= new_cost: 
                    continue 

                distance[nr][nc] = new_cost
                heapq.heappush(pq, (new_cost, nr, nc))


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    distance = [[9999 for _ in range(N)] for _ in range(N)]
    d(0,0)
    ans = distance[N-1][N-1] 
    print(f'#{tc} {ans}')
