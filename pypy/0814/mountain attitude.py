T = int(input())
for tc in range(1, T+1):
    N = int(input())

    # 지형 정보
    arr = [list(map(int,input().split())) for _ in range(N)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 봉우리의 수
    count = 0

    for r in range(N):
        for c in range(N):
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                # 유효한 인덱스 범위인지
                if 0 <= nr < N and 0<= nc < N:
                    if arr[r][c] <= arr[nr][nc]:
                        break

            else:
                count += 1

    print(f'#{tc} {count}')
