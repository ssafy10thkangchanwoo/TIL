# 재귀호출 활용
arr = [2, 4, 7, 9, 11, 19, 23]

# 문제에서 데이터가 정렬되어있다는 조건이 없으면
# 반드시 정렬부터 진행
arr.sort() 

def binarySaerch(low, high, target): 
    # 기저 조건: 언제까지 재귀호출을 반복할 것인가
    # low> high라면 데이터를 못찾음
    if low > high:
        return -1

    # low > high라면 데이터를 못찾는 경우
    else:
        mid = (low + high) //2
        
        # 1. 가운데 값이 정답인 경우
        if arr[mid] == target:
            return mid 
        # 2. 가운데 값이 정답보다 작은 경우
        elif arr[mid] < target:
            low = mid+1
            return binarySaerch(low, high, target)
        # 3. 가운데 값이 정답보다 큰 경우
        else:
            high = mid-1
            return binarySaerch(low, high, target)
    
    return "No data"


print(f'9 = {binarySaerch(0, len(arr)-1,9)}')
print(f'4 = {binarySaerch(0, len(arr)-1,4)}')
print(f'10 = {binarySaerch(0, len(arr)-1,10)}')