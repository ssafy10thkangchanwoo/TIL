T = int(input())

def dfs(n, cnt):
    global min_cnt
    # 가지치기 1: 지금 카운트가 최소카운트보다 크면 cut
    if cnt > min_cnt:
        return
    # 가지치기 2: 미래에 아무리 곱해도 따라잡을 수 없을 경우(곱셈)
    if n*2**(min_cnt-cnt) < M:
        return
    # 가지치기 3: 미래에 아무리 빼도 가망없을 때 (-10씩)
    if n - (min_cnt-cnt)*10 >M:
        return
    
    if n==M:
        min_cnt = min(min_cnt, cnt)
        return 
    
    for i in range(4):
        # +1 연산
        if i == 0:
            n += 1  
            if n<0 or n>1000000:
                break
            dfs(n, cnt+1)
            n -= 1

        # -1 연산
        if i == 1:
            n -= 1  
            if n<0 or n>1000000:
                break
            dfs(n, cnt+1)
            n += 1

        # * 2연산
        if i == 2:
            n *= 2 
            if n<0 or n>1000000:
                break
            dfs(n, cnt+1)
            n /= 2

         # -10 연산
        if i == 3:
            n -= 10  
            if n<0 or n>1000000:
                break
            dfs(n, cnt+1)
            n += 10




for tc in range(1, T+1):
    N, M = map(int,input().split())
    cnt = 0
    min_cnt = 99999
    dfs(N, cnt)
    print(min_cnt)