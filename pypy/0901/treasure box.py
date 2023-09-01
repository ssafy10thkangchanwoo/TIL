T = int(input())
for tc in range(1, T+1):
    N, K = map(int,input().split())
    numbers = list(input()) * 2
    box = set()
    for i in range(N):
        num1 = numbers[i:i+N//4]
        num2 = numbers[i+N//4:i+N//2]
        num3 = numbers[i+N//2:i+3*N//4]
        num4 = numbers[i+3*N//4:i+N]

        for n in [num1, num2, num3, num4]:
            temp = 0
            for k in range(N//4):
                temp += int(n[k], 16)*(16**((N//4-k)-1))
            box.add(temp)
    box = list(box)
    box.sort(reverse=True)
    print(f'#{tc} {box[K-1]}')
