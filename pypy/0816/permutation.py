




# numbers = [1,2,3,4,5]

# n = len(numbers)

# # i번째 원소의 자리를 바꿔가면서 순열 생성
# # 자리를 바꿀 수 있는 경우의 수

# def perm1(i):
#     # 종료 조건
#     if i == n:
#         print(numbers)
#         return
    
#     # 재귀호출

#     # 현재위치i에서 다른위치 j에 잇는 숫자와 자리를 바꾼다.
#     # j를 선택할 대는 중복을 방지하기 위해 i보다 뒤에 있는 원소만 선태
#     # i, j가 같을 수도 있다(자리를 안바꿈)
#     # i번째 원소를 누구랑 바굴지 정했다면 i+1번째 원소를 바꾸러 진행
#     for j in range(i, n):
#         # i번째와 j번째 위치를 바꾸고 진행
#         numbers[i], numbers[j] = numbers[j], numbers[i]

#         # 다음 i+1번째 원소의 자리를 바꾸러 간다.
#         perm1(i+1)

#         # i번째와 j번째 원소를 되돌려놓고 다음 진행
#         numbers[i], numbers[j] = numbers[j], numbers[i]

# perm1(0)

'''
---------------------------
'''

numbers = [1,2,3,4,5]

n = len(numbers)
# 순서의 i번째 자리를 누구로 할 것인가 직접 선택하는 방법
# i번째 자리를 누구로 선택했는지 기억해야 중복선택 안함
# selected[i] == i번째 원소를 순열을 만드는데 사용했다. # selected 자체가 순열
# selected = [0]
def perm2(i, selected):
    # 종료조건
    if i == n:
        return
    # 재귀호출
    # 현재위치i에 누구를 놓을 것인가 선택
    # 이전에 선택했던 원소는 선택 X
    for j in range(n):
        # j번째 원소를 선택한 적ㅇ ㅣ없다면 j번째 원소를 순열의 i위치에 놓기
        if numbers[j] not in selected:
            # i번째 위치에 j를 놓는다.
            selected[i] = numbers[j]
            # i번째 위치에 누굴 놓을지 정했으니 i+1번째에 누굴 놓을지 정하ㅓ 가기
            perm2(i+1, selected)
            # i번쨰 위치에 j를 놓았던 거를 없었던 일로 하고 다른 j를 선택하러 간다.
            selected[i] = 0

perm2(0, [0]*5)



# def f(i, N):
#     if i == N:
#         print(A)
#     else:
#         for j in range(i, N): # 자신부터 오른쪽 끝까지
#             A[i], A[j] = A[j], A[i]
#             f(i+1, N)
#             A[i], A[j] = A[j], A[i]

# A = [1,2,3]

# f(0, 3)