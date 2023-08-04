T = int(input())
set_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
n = 12

for tc in range(1, T+1):
    N, K = map(int, input().split())
    count = 0
    for i in range(1 << n):
        sum_sub = 0
        sum_count = 0
        for j in range(n):
            if i & (1 << j):
                sum_sub += set_a[j]
                sum_count += 1
            
        if (sum_count == N) and (sum_sub == K):
            count += 1
        
    print(f'#{tc} {count}')

