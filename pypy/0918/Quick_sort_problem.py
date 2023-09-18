def hoare_partition(left, right):
    pivot = arr[left]
    left += 1
    while True :
        while arr[left] < pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1
        
        if left >= right:
            return right 

        arr[left], arr[right] = arr[right],arr[left]

def Quick(left, right):
    if left >= right:
        return
    

    pivot = hoare_partition(left,right)
    arr[left], arr[right] = arr[right], arr[left]
    Quick(left, pivot)
    Quick(pivot +1, right)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr= list(map(int,input().split()))
    Quick(0, len(arr)-1)
    
    A = arr 
    print(f'{tc} {A[N//2]}')
