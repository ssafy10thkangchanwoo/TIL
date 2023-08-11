T= int(input())

def reading(arr):
    # 열 판독
    for i in range(N):
        counts = 0
        for j in range(N):
            if arr[i][j] == 'o':
                counts += 1
            else:
                counts = 0
            # 5 이상이면 출력
            if counts >= 5:
                return 'Yes'
    # 행 판독
    for j in range(N):
        counts = 0
        for i in range(N):
            if arr[i][j] == 'o':
                counts += 1
            else:
                counts = 0
            # 5 이상이면 출력
            if counts >= 5:
                return 'Yes'


    # 대각선 판독 좌->우
    for k in range(N):
        for i in range(N-k):
            for j in range(k, N):
                if arr[i][j] == 'o':
                    counts += 1
                else:
                    counts = 0
                # 5 이상이면 출력
                if counts >= 5:
                    return 'Yes'
    #
    # 대각선 판독 2
    for k in range(N):
        for j in range(k, N):
            for i in range(N-k):
                if arr[i][j] == 'o':
                    counts += 1
                else:
                    counts = 0
                # 5 이상이면 출력
                if counts >= 5:
                    return 'Yes'
    #
    # # 대각선 판독  좌
    #
    # for o in range(N-4):
    #     for p in range(N - 4):
    #         for n in range(5):
    #             for m in range(5):
    #                 if arr[o+n][p+m] == 'o':
    #                     counts += 1
    #                 else:
    #                     counts = 0
    #                 # 5 이상이면 출력
    #                 if counts >= 5:
    #                     return 'Yes'
    #
    # #대각선판독 (역)
    #
    # for o in range(N-4):
    #     for i in range(o, N+o):
    #             if arr[i][-i] == 'o':
    #                 counts += 1
    #             else:
    #                 counts = 0
    #             # 5 이상이면 출력
    #             if counts >= 5:
    #                 return 'Yes'






    else:
        return 'No'


for tc in range(1, T+1):
    N = int(input())

    arr = [input() for _ in range(N)]

    result = reading(arr)

    print(f'#{tc} {result}')


