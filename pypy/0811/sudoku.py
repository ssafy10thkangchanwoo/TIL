def sudoku(arr):
    for i in range(9):
        cnt = [0]*10
        for j in range(9):
            cnt[arr[i][j]] += 1

        for k in range(1, 10):
            if not cnt[k] == 1: # 1~9 사이 숫자가 1이 아니면
                return 0 # 0 리턴


    for j in range(9):
        cnt = [0]*10
        for i in range(9):
            cnt[arr[i][j]] += 1
        for k in range(1,10):
            if not cnt[k] == 1: # 1~9 사이 숫자가 1이 아니면
                return 0 # 0 리턴

    for i in range(0, 9, 3):
        cnt = [0]*10
        for j in range(0, 3):
            for k in range(0, 3):
                cnt[arr[i+j][i+k]] += 1
        for l in range(1,10):
            if not cnt[l] == 1: # 1~9 사이 숫자가 1이 아니면
                return 0 # 0

    else:
        return 1



T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int,input().split())) for _ in range(9)]

    ans = sudoku(arr)

    print(f'#{tc} {ans}')


    # ans = 1 # 수도쿠가 완성되면 1, 아니면 0

    # for i in range(9):
    #     cnt = [0]*10
    #     for j in range(9):
    #         cnt[arr[i][j]] += 1
    #     for k in range(1, 10):
    #         if cnt[k] == 0: # 1~9 사이에 빠진 숫자가 있으면
    #             ans = 0
    #             break # for k
    #     if ans ==0:
    #         break
    #

