# N = 2
# M = 4
# arr = [[0, 1, 2, 3], [4, 5, 6, 7]]
# for i in range(N):
#     for j in range(M):
#         print(arr[i][j + (M-1-2*j)*(i%2)])

# arr = [[0]*M for _ in range(N)]
# arr2 = [[0]*M]*N ## 안돼    # 근데 첨에 [0]*M은 왜 괜찮지?
# # arr[0][0] = 1 # [[1, 0, 0, 0], [0, 0, 0, 0]]
# # arr2[0][0] = 1  # [[1, 0, 0, 0], [1, 0, 0, 0]]
# arr = [0]*4
# arr[0] = 1
# print(arr)

# print(arr)
# print(arr2)

# max_v = 0
# arr = [[0,1,2,3][4,5,6,7]]
# for i in range(N):
#     row_total = 0 # 각 행의 합
#     for j in range(M):
#         row_total += arr
#     if max_v < row_total:
#         max_v = row_total

# '''
# 3
# 1 2 3
# 4 5 6
# 7 8 9
# '''
# di = [0, 1, 0, -1]
# dj = [1, 0, -1, 0]
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
#
# max_v = 0 # 모든 원소가 0 이상이라면
# for i in range(N): # 모든 원소 arr[i][j]에 대해
#     for j in range(N):
#         # arr[i][j] 중심으로
#         s = arr[i][j]
#         for k in range(4):
#             ni, nj = i+di[k], j+dj[k]
#             ni, nj = i+di*p, j+dj*p
#             if 0<=ni<N and 0<=nj<=N: # 배열을 벗어나지 않으면
#                 s += arr[ni][nj]
#         #여기까지가 주변 원소를 포함한 합
#         if max_v < s :
#             max_v = s