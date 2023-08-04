T = int(input())

for tc in range(1, T+1):
    # 바운스 챌린지 횟수
    N = int(input())
    numbers = list(map(int,input().split()))

    # 총합
    result = 0
    # 챌린지는 n번 실행
    # N번 시도할 때마다 합을 구하는 방식이 다르다.
    for i in range(N):
        # i 번째 챌린지 합을 구하는 방식.
        # i+1만큼 움직이면서 합을 구한다.
        for j in range(0, N, i+1):
            result += numbers[j]

    # result값이 0이상이면 그대로 사용하고 음수이면 0으로 바꾼다.
    result = result if result >=0 else 0
    print(f'#{tc} {result}')
