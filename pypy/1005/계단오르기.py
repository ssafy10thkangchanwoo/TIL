N = int(input())
start = int(input())
if N ==0:
    print(0)
else:

    dp = [[0,0,0] for _ in range(N+1)]

    for i in range(1, N):
        a = int(input())
        dp[i][0] = dp[i-1][2]
        dp[i][1] = dp[i-1][0] + a 
        dp[i][2] = dp[i-1][1] + a

    answer = max(dp[N-1][1],dp[N-1][2])
    print(answer)