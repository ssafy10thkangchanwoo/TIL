for tc in range(1, 11):
    t = int(input())

    # 암호문자열
    password = list(map(int,input().split()))

    # 암호의 길이
    N = 8

    # 큐 생성(원형)
    q = [0] * (N + 1)
    front = rear = 0

    # 처음 n번 큐에 넣기
    for i in range(N):
        rear = (rear + 1) % N
        q[rear] = password[i]

    # 빼줄 숫자
    number = 1

    while True:
        # 비밀번호 하나 꺼내서
        # number 를 빼준후에 다시 큐에 넣기
        front = (front+1) % N
        item = q[front]

        item -= number

        # 숫자를 빼와서 감소시켰는데
        # 만약 0이하가 되어버렸다면 비밀번호가 완성된 것
        # 숫자를 0으로 바꾸고 큐의 맨 뒤에 넣은 다음 종료
        if item <= 0:
            item = 0
            rear = (rear+1) % N
            q[rear] = item
            break
        else:
            # 0보다 크다면
            rear = (rear+1) % N
            q[rear] = item

            # 다음 뺄 수를 1씩 증가
            number += 1
            # 싸이클 계산
            if number > 5:
                number = 1

    # 원형큐에서 dequeue를 8번 하면 된다.
    for i in range(8):
        front = (front+1)%N


