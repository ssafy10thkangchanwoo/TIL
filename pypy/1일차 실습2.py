# T = int(input())
# N, M = map(int, input().split(','))
# nums = list(map(int,input().split()))
#
#
# for i in range(0, N-M+1):
#     connec_sum = nums[i] + nums[i+1] + nums[i+2]
#     print(connec_sum)


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    nums = list(map(int,input().split()))

    for i in range(0, N-M+1):
        connec_sum = sum(nums[i:i+M])

        print(connec_sum)