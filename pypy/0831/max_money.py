def swap(cnt):
    global max_v
    n = int(''.join(numbers))
    if cnt % 2 == 0 and n == big_num:
        max_v = max(max_v, n)
        return
    elif cnt==times:
        
        
        max_v = max(max_v, n)
        return
    
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            numbers[i], numbers[j] = numbers[j], numbers[i]
            swap(cnt+1)
            numbers[i], numbers[j] = numbers[j], numbers[i]
def BIG(test):
    test.sort(reverse=True)
    return int(''.join(test))


T = int(input())
for tc in range(1,T+1):
    numbers, times = list(map(int,input().split()))
    numbers = (list(str(numbers)))
    test = (list(str(numbers)))
    cnt = 0
    max_v = 0
    big_num = BIG(test)
    swap(0)
    print(f'#{tc} {max_v}')