numbers = [1,2,3,4,5]
selected = [0] * 5
# selected[i] == 1: 내가 i번째 원소를 부분집합에 포함시켰다.
# selected[i] == 0: 내가 i번째 원소를 부분집합에 포함시키지 않았다.

n = len(numbers)
# 만약 합이 x보다 작은 부분집합만 구해야 한다면??
x = 6


# 재귀함수로 부분집합 구하기
# i번째 원소를 부분집합에 포함할지 안할지를 결정한다.
# n-1번째 원소까지 하면 된다.

# n-1번째 원소까지 완료한 경우에뒤로 돌아와서 내가 이전에 선택했다면
# 선택하지 않고 진행->반복


# 내가 i번째 원소를 선택 or 선택하지 않았던 상황에서 합을 기억

def subset(i, n, subsum):
    # 0 . 다른조건(최적화)
    if subsum > x:
        return 
    
    # 1. 종료조건
    if i == n:


        # n개의 원소에 대한 선택을 끝냈다.
        temp = 0
        for j in range(n):
            if selected[j]:
                temp += numbers[j]
        # 합이 x 이하인 부분집합만 출력
            if temp <= x:
                for j in range(n):
                    if selected[j]:
                        print(numbers[j], end = '')
                print()
            return

            
    
    # 2. 재귀호출
    # i번째 원소를 선택하고 다음 i+1번째 운소를 선택하러 가거나
    selected[i] = 1
    subset(i + 1, n, subsum + numbers[i]) # #return이 되었다..?
    # i번째 원소를 선택하지 않고 다음 i+1번째 원소를 선택하러 가거나
    selected[i] = 0
    subset(i + 1, n, subsum)


subset(0, n, 0)





# def f(i, N):

#     if i == N:
#         s = 0
#         print(bit, end = ' ')
#         for j in range(N):
#             if bit[j]:
#                 s += A[j]
#                 print(A[j], end = ' ')
#         print(f' :{s}')

#         return
#     else:
#         bit[i] = 1
#         f(i+1, N)
#         bit[i] = 0
#         f(i+1, N)
#         return

# A = [1, 2, 3]
# bit = [0]*3
# f(0, 3)

