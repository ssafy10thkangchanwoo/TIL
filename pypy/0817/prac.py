T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    pizza_list = list(map(int,input().split()))
    next_i = 0 # 굳이 필요할까?
    oven = [0]* 1000
    front = rear = -1

    for i in range(N):
        rear += 1
        oven[rear] = [i, pizza_list[i]]
        next_i += 1

    remain = N

    last_idx = -1

    while True:
        if oven