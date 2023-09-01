def perm(i, times):
    if i == len(numbers):
        return 
    
    for j in range(i, len(numbers)):
        numbers[i], numbers[j] = numbers[j], numbers[i]
        times += 1
        
        perm(i+1,times)
        numbers[i], numbers[j] = numbers[j], numbers[i]


+change
T = int(input())
for tc in range(1,T+1):
    numbers, times = list(map(int,input().split()))
    numbers = (list(str(numbers)))
    print(perm(0,times))