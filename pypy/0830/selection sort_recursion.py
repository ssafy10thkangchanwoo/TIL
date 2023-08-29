def selection_sort(i, lst): # i번째 자리에 i번째로 작은 원소를 놓겠다.
    # 종료조건
    if i == 5:
        return

    # 해야할 일 : 제일 작은값 찾아서 i번째 인덱스에 놓기 (자리교환)

    min_idx = i
    for n in range(i+1, len(lst)):
        if lst[i] > lst[n]:
            min_idx = n
    lst[i], lst[min_idx] = lst[min_idx], lst[i]
    # 재귀호출 (i+1) 번 인덱스에 놓을 작은 원소 찾기
    selection_sort(i+1, lst)

lst = [3,2,4,5,1]

# 재귀 호출 시작 : 0번째 자리에 놓을 제일 작은 원소 찾기
selection_sort(0,lst)

print(lst)