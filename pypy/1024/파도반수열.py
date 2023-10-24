T = int(input())
for tc in range(1, T+1):
    N = int(input())
    list = [1,1,1,2,2,3,4,5,7,9]+[0]*N
    for i in range(1, N):
        if i >= 5:
            list[i] = list[i-1]+list[i-5] 

    print(f'#{tc} {list[N-1]}')