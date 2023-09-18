def merge(left, right):
    result = []

    while len(left)>0 or len(right) >0:
        if len(left) > 0 and len(right)>0:
            if left[-1] > right[-1]:
                cnt += 1
            if left[0] <= right[0]:
                
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        
        elif len(left)>0:
            result.append(left.pop(0))
        
        elif len(right)>0:
            result.append(right.pop(0))

    return result


def merge_sort(numbers):
    if len(numbers) == 1:
        return numbers
    
    left = []
    right = []
    middle = len(numbers)//2

    for el in numbers[:middle]:
        left.append(el)
    
    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int,input().split()))
    merge_sort(numbers)
    cnt = 0
    print(f'#{tc} {cnt}')
