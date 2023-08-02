T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = input()

    # 카운트배열 사용, 등장하는 숫자의 범위가 0~9
    # count[i]가 의미 하는 것은 numbers에서 숫자 i가 등장한 횟수
    counts = [0] * 10

    for n in numbers:
        counts[int(n)] += 1 # n이 등장한 횟수만큼 1씩 증가


    # 최대 개수
    max_count = 0

    # 가장 큰수
    max_num = 0

    # 0 ~ 9 까지의 숫자들 중에서 가장 자주 등장한 숫자가 무엇인가??
    # 그리고 등장한 횟수가 같다면 그중에 큰 거 골라서 출력

    for i in range(10):
        if counts[i] >= max_count:
            # 숫자 i가 등장하는 횟수가 내가 알고 있던 최대 횟수보다 많으면
            # 최대값 갱신
            max_count = counts[i]
            max_num = i

    print(f'#{tc} {max_num} {max_count}')
