T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # 농작물 정보
    field = [list(map(int, input())) for _ in range(N)]

    # 수확한 농작물
    crops = 0

    # 밭의 정 중아과의 거리가 d 이하인 곳만 수확
    d = N//2
    # 중앙좌표
    center = (d,d)

    for r in range(N):
        for c in range(N):
            # 거리 계산 방법
            # |r-d| + |c-d| <= 3이면 농작물을 수확한다.
            if abs(r-d) + abs(c-d) <= d:
                crops += field[r][c]

    print(f'#{tc} {crops}')