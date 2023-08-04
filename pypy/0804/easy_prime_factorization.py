T = int(input())
for tc in range(1, T+1):
    N = int(input())
    count_2 = 0
    count_3 = 0
    count_5 = 0
    count_7 = 0
    count_11 = 0

    while N != 1: # 45
        if N % 2 == 0: # 불만족
            count_2 += 1
            N /= 2

        elif N % 3 == 0: # 만족
            count_3 += 1 # 3에 대한 카운트+ 1 +2
            N /= 3  # 15

        elif N % 5 == 0:
            count_5 += 1
            N /= 5

        elif N % 7 == 0:
            count_7 += 1
            N /= 7

        elif N % 11 == 0:
            count_11 += 1
            N /= 11


    count_num = f'{count_2} {count_3} {count_5} {count_7} {count_11}'

    print(f'#{tc} {count_num}')