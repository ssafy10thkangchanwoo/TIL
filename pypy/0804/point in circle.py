T = int(input())

for tc in range(1, T+1):
    N = int(input())
    count = 0
    for x in range(-N, N+1):
        for y in range(-N, N+1):
            if N**2 >= x**2+y**2:
                count += 1

    print(f'#{tc} {count}')

