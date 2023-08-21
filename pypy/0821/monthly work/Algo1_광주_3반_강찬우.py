T = int(input())
# 테스트 케이스 개수
for tc in range(1, T+1):
    # 격자의 크기
    N = int(input())
    # 격자 정보 입력
    matrix = [list(map(int,input().split())) for _ in range(N)]
    # 최대값 및 최소값
    max_pang = 1
    min_pang = N*N*9

    # 각 행,열 탐색
    for r in range(N):
        for c in range(N):
            # maze[r][c]값(중앙) 및 그 사방에 범위
            s = matrix[r][c]
            near_pang = 0
            for i in range(4):
                for j in range(1, s+1):
                    # 사방탐색에 필요한 변수(상하좌우)
                    dr = [-j, j, 0, 0]
                    dc = [0, 0, -j, j]
                    # 사방에 대한 값
                    nr = r + dr[i]
                    nc = c + dc[i]
                    # 사방에 대한 값이 격자 내부에 있는지에 대한 여부 확인
                    # 격자 내부에 있다면 합산
                    if 0 <= nr < N and 0 <= nc < N:
                        near_pang += matrix[nr][nc]
            if max_pang < near_pang + s:
                max_pang = near_pang + s
            if min_pang > near_pang + s:
                min_pang = near_pang + s
    # 최대값 및 최소값 차
    answer = max_pang - min_pang
    # 결과 산출
    print(f'#{tc} {answer}')