T = int(input())
matrix = [[0]*10 for _ in range(10)]

for tc in range(1, T+1):

    wow = 0
    end_r = 9
    end_c = 9
    for tc in range(1, T+1):
        for j in range(0, 10):
            if matrix[end_r][j] == 2:
                end_c = j

        for i in range(end_c, -1, -1):
            if matrix[end_r][end_c-1] == 1:
                end_c -= 1

            if matrix[end_r][end_c+1] == 1:
                end_c += 1

            else:
                end_r -= 1

            if end_r == 0:
                wow = end_c

    print(f'#{tc} {wow}')
