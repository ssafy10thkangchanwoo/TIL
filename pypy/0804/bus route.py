T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt = [0]*5000 # 1~5000번 각 정류장을 지나는 노선 수
    for _ in range(N):
        A, B = map(int, input().split())
        # cnt[A:B+1] += 1
        for i in range(A, B+1):
            cnt[i] += 1
    
    P = int(input())
    bus_stop = [int(input()) for _ in range(P)]
    print(f'#{tc}', end= '')
    for x in bus_stop:
        print(cnt[x], end = '')
    print() # 줄 바꿈
         
              