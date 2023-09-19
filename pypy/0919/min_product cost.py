def fac(i, nums, cost):
    global min_c
    if i == N:
        min_c = min(min_c, cost)
        return
    else:
        for j in range(N):
            if j not in nums:
                cost += matrix[i][j]
                
                if cost < min_c: 
                    
                    fac(i+1, nums+ [j], cost)
                    cost -= matrix[i][j]
                
            
T = int(input())
for tc in range(1, T+1):
    N= int(input())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    nums = []
    visited = [0] * N
    cost = 0
    min_c = 9999
    fac(0,nums,cost)

    # for sub in sub_nums:
    #     cost= 0
    #     for i in range(N):
    #         cost += matrix[i][sub[i]-1 ] # sub는 인덱스처럼 사용할거니까..
    #                                     # 따로 구한 숫자들을 다시 리스트처럼 사용할 때 주의
    #     min_c = min(cost, min_c)
    print(f'#{tc} {min_c}')
    