T = int(input())

for tc in range(1, T+1):
    # N은 오븐크기, M은 피자개수
    N, M = map(int, input().split())
    # 우리가 구워야할 치즈 정보
    pizza_list = list(map(int, input().split()))
    # 다음에 꺼내올 피자 인덱스
    next_i = 0
    # 오븐을 큐로 만들어보자
    oven = [0]* 1000
    front = rear = -1

    # 오븐의 크기만큼 피자 넣어주기
    for i in range(N):
        # 오븐에 피자 넣기
        rear += 1
        # 나중에 꺼낼때를 위해서 피자 번호도 같이 넣기
        oven[rear] = [i, pizza_list[i]] [ # [피자번호, 치즈 양]
        next_i += 1

    # 오븐에 남아있는 피자의 개수
    remain = N

    # 마지막에 꺼낸 피자의 번호
    last_idx = -1

    # 모든 피자의 치즈가 녹을 때까지 반복
    while True:
        # 피자를 하나 꺼내서
        front += 1
        pizza_idx, pizza = oven[front]
        # 치즈를 녹이고
        pizza //= 2

        # 남은 치즈의 양이 0이 아니다 ==> 다시 오븐에 넣기
        if oven[rear] += 1:
            rear += 1
            oven[rear] = [pizza_idx, pizza]

        # 남은 치즈 양이 0이 되었다
        else:
            if next_i <m:
                rear += 1
                oven[rear] = [next_i, pizza_list[next_i]]
                # 하나 꺼냈으니 다음에 꺼내올 피자 번호
                next_i += 1

            # 현재 오븐의 자리에 남은 피자 하나 꺼내서 넣기
            rear += 1

            oven[rear] = [i, pizza_list[i]]  # [피자번호, 치즈 양]
            next_i += 1
            # 넣을 피자가 없다
            else:

                # 오븐에 남은 피자도 없는 상황이 온다.
                # 현재 피자의 번호가 답이 된다.
                # 답을 구하고 반복 종료


# T = int(input())
# def input_pizza(i):
#     global s
#
#     oven[i] = cheese[s]
#     s += 1
#     return oven[i]
#
# def heating(oven):
#     for i in range(N):
#         if oven[i] == 0:
#             oven[i] = input_pizza(s)
#
#         oven[i] = oven[i]//2
#
# for tc in range(1, T+1):
#     N, M = map(int,input().split())
#     cheese = list(map(int, input().split()))
#     oven = [0] * N
#     s = 0
#
#     if oven[]
#
#
