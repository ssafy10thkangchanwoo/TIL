T = int(input())

for tc in range(1, T+1):
    pattern = input()
    text = input()
    max_count = 0
    for i in range(len(pattern)):
        counts = 0
        for j in range(len(text)):
            if pattern[i] == text[j]:
                counts += 1

            if counts > max_count:
                max_count = counts

    print(f'#{tc} {max_count}')

