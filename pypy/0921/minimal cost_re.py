from heapq import heappush, heappop


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())

def dijkstra():
    q = []
    # 좌측 상단 시작이니까 위치 0,0 
    # 가중치도 0으로 시작
    fuel[0][0] = 0 
    heappush(q, (0,0,0))

    while q:
        # w: 가중치
        # r,c : 행번호, 열번호
        w, r, c = heappop(q)

        # 방금 꺼내온 r,c까지의 사용량 w가 
        # 이전에 계산해놓은 r,c까지의 사용량보다 작으면 진행할 필요 없다.
        if fuel[r][c] < w: 
            continue

        # r,c와 인접한 위치 탐색 
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0<= nr < N and 0<= nc < N:
                # nr, nc가 갈 수 있는 위치

                # nr, nc가 r,c보다 높은지 계산
                height_diff = 0 
                if arr[nr][nc] > arr[r][c]:
                    heigh_diff = arr[nr][nc] - arr[r][c]
                
                # nr, nc 까지 이동하는데 사용한 연료량 = r,c까지 이동하는데 사용한 연료량 + 기본사용량(1)+높이차이량(height_diff)
                # 이전에 계산해놓은 nr, nc까지 이동하는데 사용한 연료량보다 작으면 갱신
                cost = fuel[r][c] + height_diff + 1
                if cost<fuel[nr][nc]:
                    fuel[nr][nc] = cost
                    # 갱신이 일어날 때만 추가
                    heappush(q, (cost,nr,nc))


for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    fuel = [ [10000000] *N for _ in range(N)]  

    dijkstra()
    print(f'#{tc} {fuel[N-1][N-1]}')