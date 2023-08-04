T = int(input())

# d = 0 오른쪽
# d = 1 아래
# d = 2 왼쪽
# d = 3 위쪽

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
for tc in range(1, T+1):
    N = int(input())

    # 달팽이집을 0으로 다 채워서 N*N만큼 만들어주기

    snail = [[0]*N for _ in range(N)]

    #  달팽이집 채우기 (0,0) 고정
    # N * N번 반복하면서 채워 간다.
    # 방향은 우->하->좌->상->우->,...

    # d는 현재 채워 나가는 방향
    d = 0
    r, c = 0, 0

    for i in range(N*N+1):
        snail[r][c] = i

        # 다음 방향으로 진행
        # 다음 위치가 유효한 위치인지
        nr = r + dr[d]
        nc = c + dc[d]

        # 다음 위치가 유효하지 안흥면 방향 꺽기
        # nr, nc가 인덱스 범위 안에 있어야 하고
        # 다음 위치가 0이 아니면 방향 꺽기
        if 0<= nr <N and 0<= nc < N and snail[nr][nc] ==0:
            # 인덱스 유효한지 먼저 확인. <단축평가 참조>
            # 다음 위치가 유효하면 계속 가고
            r, c = nr, nc
        else:             
            # 유효하지 않으면 방향 꺽기
            # d = d+1 if d < 3 else 0
            # if d<3:
                # d = d+1
            # else:
            #   # d = 0
            d = (d + 1)%4
            r = r + dr[d]
            c = c + dc[d]

    # print(*snail, set"\n")
    for i in range(N):
        print("".join(map(str,snail[i])))


