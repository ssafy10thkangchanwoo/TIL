T = 10

for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(8)]

    # 열부터
    for i in range(8):
        for j in range(9-N):
            word = ''
            for k in range(j):
                word += arr[i][j+k]

