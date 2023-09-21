from collections import deque 
T = int(input())


def bfs(n):
    q = deque()

    v =[0]*(1000000+1)
    v[n] = 1
    q.append(n)

    # 연산횟수
    cnt = 0

    # bfs 
    while q:
        # bfs  단계 나누기
        size = len(q)
        # size만큼 반복하면 한 단계 끝
        for _ in range(size):
            a = q.popleft()
            if a == M:
                return cnt 
            for i in (a+1, a-1, a*2, a-10):
                if 1<= i <= 1000000 and v[i] ==0:
                    q.append(i)
                    v[i] = 1
            
        cnt += 1


for tc in range(1, T+1):
    N, M = map(int,input().split())
    print(f'#{tc} {bfs(N)}')