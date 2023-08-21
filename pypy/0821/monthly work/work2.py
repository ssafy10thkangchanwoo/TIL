T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    A = list(input().split())
    B = [] # 홀 큐
    C = [] # 짝 스택

    # 보너스 숫자
    bonus = 0

    # 리스트의 길이만큼 반복하여 숫자를 꺼내서
    # 보너스 숫자를 더한 다음
    # 홀수면 큐에 넣고 짝수면 스택에 넣는다.

    for i in range(N):
        if A[i] == '+':
            bonus += 1
        else:
            num = int(A[i]) + bonus
            if num % 2 :
                B.append(num)
            else:
                C.append(num)

    # M번까지 숫자를 꺼내서 확인
    for i in range(M):
        # 큐에서 꺼낸 숫자
        from_que = B.pop(0) if B else 0

        # 스택에서 꺼낸 숫자
        from_stack = C.pop(0) if C else 0

    print(f'#{tc} {from_que+from_stack}')