#
# import sys
# sys.stdin = open("in.txt", "r")
#

#
# def _is_valid(i, j):
#     return 0<= i < N and 0<= j < N

T= int(input())

for tc in range(1, T+1):
    N = int(input())
    #상하좌우(델타)
    #(행의 좌표, 열의 좌표)
    #(i, j)
    # 상(-1, 0) 하(1,0) 좌(0,-1) 우(0, 1)
    dr = [-1, 1, 0, 0]# 행 번호의 변화량
    dc = [0, 0, -1, 1]# 열 번호의 변화량

    # 2차원 배열 입력받기
    # list(....) => 한줄 입력받기 (1차원 배열)
    # for _ in range(N) => N번 입력을 받아서 2차원 배열로 만든다.

    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 2차원 배열 탐색
    # 행 우선으로

    diff_sum = 0
    for i in range(N): # 가로와 세로의 길이가 같으니까 행, 열 다 N
        for j in range(N):

            # 현재 위치가 i행 j열 (i, j)
            # matrix[i][j] =>현재 위치에 저장된 원소
            print(f"현재 위치 : {i},{j}), 값 : {matrix[i][j]}")
            # 현재 위치에서 상하좌우 절대값의 합
            now_diff_sum = 0

            for d in range(4):
                # d 는 델타 배열의 인덱스, d = 0 이면 상
                nr = i + dr[d]
                nc = j + dc[d]
                if 0 <= nr < N and 0 <= nc < N:
                    if matrix[i][j] - matrix[nr][nc] >= 0:
                        now_diff_sum += matrix[i][j] - matrix[nr][nc]
                    else:
                        now_diff_sum -= matrix[i][j] - matrix[nr][nc]

    diff_sum+=now_diff_sum
    print(diff_sum)




                # 내가 계산한 위치가 유효안 인덱스인지(배열이 범위 안에 있는지) 검사
                # if 0 <= nr < N and 0 <= nc < N:
                #     pass
