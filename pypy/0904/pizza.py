T = int(input())

for tc in range(1, T+1):

    N, M = map(int,input().split())
    pizza_list = list(map(int, input().split()))
    pizza_king = 0
    zero = 0
    print(pizza_list.count(True))
    while True:
        # if pizza_list.count(True)<=N:
        
        if len([x for x in pizza_list if x > 0]) <= N:
            pizza_king = max(pizza_list)

            king_idx = pizza_list.index(pizza_king)
            break
        
        else:
            zero=pizza_list.count(0) 
            for i in range(N+zero):
                pizza_list[i] = pizza_list[i]//2



        
    print(f'#{tc} {king_idx}')

