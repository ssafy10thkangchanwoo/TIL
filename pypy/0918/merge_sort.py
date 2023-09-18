
def merge(left, right):
    result = [] # 왼쪽과 오른쪽을 합친 결과

    # i,j : i=> 왼쪽 리스트에서 원소를 꺼낼 위치, 
    # j => 오른쪽 리스트에서 원소를 꺼낼 위치

    # 왼쪽과 오른쪽 둘중에 하나라도 원소가 남아있으면 진행
    while len(left)>0 or len(right) >0 :
        # 둘 다 원소가 남아있으면 누구꺼를 꺼내올건지 비교
        if len(left) > 0 and len(right)> 0 :
            # 왼쪽의 맨 앞 원소가 오른쪽의 맨 앞 원소보다 작으면 왼쪽 맨 앞에 넣기
            if left[0] <= right[0]:
                result.append(left.pop(0))
            # 그게 아니면 오른쪽 맨 앞 넣기
            else:
                result.append(right.pop(0))

        
        # 왼쪽만 남아있으면 왼쪽 남은거 다 추가
        elif len(left) > 0:
            result.append(left.pop(0))
        
        # 오른쪽만 남아있으면 오른쪽 남은거 다 추가
        elif len(right)>0:
            result.append(right.pop(0))

    return result

A = [69,10,30,2,16,8,31,22]

def MergeSort(list):

    m = len(list)

    # 종료조건 (더 이상 분할 못 할 때까지)
    if m ==1:
        return list
    

    # 분할
    mid = m//2 
    left, right = list[:mid], list[mid:] # 얕은 복사

    # 정복
    left = MergeSort(left) # 왼쪽 정렬
    right = MergeSort(right) # 오른쪽 정렬




    # 병합
    return merge(left,right)

print(MergeSort(A))
