T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split()) # N:손님수, M초마다 K개 생산
    arr = map(int,input().split()) # N명이 도착하는 시간
    result = 'Possible'
    bread = [0]*100
    for i in range(101):
        if not i//M:  
            bread[i] = K*(i//M)
        else:
            bread[i] = 0
            # result = 'Impossible'
    
    for j in range(N):
        if bread[arr[j]]:
            bread[arr[j]:] 















# T = int(input())
# for tc in range(1, T+1):
#     N, M, K = map(int, input().split()) # N:손님수, M초마다 K개 생산
#     arr = list(map(int,input().split())) # N명이 각각 도착하는 시간
#     arr.sort()  # 도착시간 순으로 정렬

#     result = 'Possible'
#     for i in range(N):
#         if i+1 > arr[i]//M*K:
#             result = 'Impossible' #i번째 손님이 왔을 때 생산량
#             break

#     print(f'{tc} {result}')