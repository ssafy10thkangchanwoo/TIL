T = 10
for _ in range(1, T+1):
    tc = input()
    numbers = list(map(int, input().split()))
    n_sum = sum(numbers)
    matrix = numbers + [0]*(n_sum+1)
    front = -1
    rear = 7


    while matrix[rear] > 0:
        for i in range(1, 6):
            front += 1
            rear += 1
            matrix[rear] = matrix[front] - i
            if matrix[rear] <= 0:
                break


    answer = matrix[front:rear]
    print(f'#{tc} {answer}')



