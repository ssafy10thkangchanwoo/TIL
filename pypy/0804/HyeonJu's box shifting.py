T = int(input())

for TC in range(1, T+1):
    N, Q = map(int,input().split())
    arr = [0]*N
    print_arr = ''
    # Q번 케이스 입력받을 것임.
    for t in range(1, Q+1):
        L, R = map(int,input().split())
        for s in range(L-1, R):
            arr[s] = t

    for i in arr:
        print_arr += str(i)+' '
    print(f'#{TC} {print_arr}')