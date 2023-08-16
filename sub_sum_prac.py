def f(i, N, s): # s: i-1원소까지 부분집합의 합(포함된 원소의 합)
    global cnt
    cnt += 1
    if i == N:
        if s == 10:
            print(bit)
        print(bit, end = ' ')
        print(f' :{s}')
        return
    else:
        bit[i] = 1 # 부분집합에 A[i] 포함
        f(i+1, N, s+A[i]) 
        bit[i] = 0 # 부분집합에 A[i] 미포함
        f(i+1, N, s)
        return
#
# # 1부터 10까지 수를 원소로 가지는 집합. 부분집합의 합이 10인 경우
# N = 10
# A = [i for i in range(1, N+1)]
# cnt = 0
# bit = [0]*N
# f(0, 3, 0)
# print(cnt)
#
# numbers = [1,2,3,4,5]
#
# selected = [0]*5
# # selected[i] == 1: 부분집합포함
# n = len(numbers)
# x = 6 # 부분집합 합 비교 변수
#
# def subset(i, n, subsum):
#     if subsum>x:
#         return
#
#     if i == n:
#         temp = 0 # 임시비교변수
#         for j in range(n):
#             if selected[j]:
#                 temp += numbers[j]
#
#         if temp <= x:
#             for j in range(n):
#                 if selected[j]:
#                     print(numbers[j], end= " ")
#                 print()
#         return