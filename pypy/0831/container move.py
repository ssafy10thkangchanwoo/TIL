T = int(input())
for tc in range(1, T+1):
    C, T = map(int,input().split())
    c = list(map(int,input().split()))
    t = list(map(int,input().split()))
    c.sort(reverse=True)
    t.sort(reverse=True)
    i = 0
    j = 0
    total = 0
    while True:
        if i >= len(c) or j >= len(t):
            break
        if c[i] <= t[j]: # 실을 수 있다.
           total += c[i]
           i += 1
           j += 1
        else:
            i += 1
    
    print(f'#{tc} {total}')