T = int(input())
for tc in range(1,T+1):
    N = int(input())
    numbers = list(map(int,input().split()))
    numbers.sort()
    min_v = 1000

    for i in range(0, N-2):
        if (i+1)//2 <= N//2:
            for j in range(i+1, N-1):
                if (j-i)//2 <= N//2 and N-1-j//2 <= N//2:
                    small = i+1
                    mid = j-i 
                    large = N-1-j 
    
                    if small <= N//2 and mid <= N//2 and large <= N//2:
                        if numbers[i] != numbers[i+1] and numbers[j]!=numbers[j+1]:
                            if min_v > max(small, mid, large) - min(small, mid, large):
                                 min_v = max(small, mid, large) - min(small, mid, large)
        

    # for i in range(0, N-2):
    #         for j in range(i+1, N-1):
    #             if numbers[i] != numbers[i+1] and numbers[j]!=numbers[j+1]:
    #                 # 같은 크기의 당근은 같은 크기의 상자에 들어있어야 한다.
    #                 # 다른 크기의 상자에는 다른 크기의 당근이 들어있어야 한다.
    #                 # -> small에는 i개의 당근이 들어있다. i+1번째 당근은 mid에 들어있다.
    #                 #  i번째 당근과 i+1번째 당근이 크기가 같으면 안된다.
    #                 small = i+1
    #                 mid = j-i 
    #                 large = N-1-j 
    #                 if small <= N//2 and mid <= N//2 and large <= N//2:
    #                      if min_v > max(small, mid, large) - min(small, mid, large):
    #                           min_v = max(small, mid, large) - min(small, mid, large)
        
    if min_v == 1000:
        min_v = -1
        
    print(f'#{tc} {min_v}')
