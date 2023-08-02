T = 10

for tc in range(1, T+1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]
    max_j = 0
    max_i = 0
    max_ii = 0
    max_ri = 0
    max_all = 0
    # 행 합 중 최대
    for i in range(100):
        max_i = 0
        for j in range(100):
            max_i += matrix[i][j]
            if max_all < max_i:
                max_all = max_i

    # 열 합 중 최대
    for j in range(100):
        max_j = 0
        for i in range(100):
            max_j += matrix[i][j]
            if max_all < max_j:
                max_all = max_j

    # 대각선 합 중 최대
    for i in range(100):
        max_ii += matrix[i][i]
        if max_all < max_ii:
            max_all = max_ii

    # 역 대각선 합 중 최대
    for i in range(100):
        max_ri += matrix[i][99-i]
        if max_all < max_ri:
            max_all = max_ri

    print(f"#{tc} {max_all}")





