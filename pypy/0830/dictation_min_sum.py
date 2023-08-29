dr = [0, 1] # 방향이동용 리스트
dc = [1, 0]

def is_valid(r,c):
    return 0<=r<N and 0<= c < N # r,c가 자판 안에 있는가?

# 내 위치가 (0,0)일 때 합 -> solve(0,0) (0,0)일 때 합
# 내 위치가 (1,0)일 때 합 -> solve(1,0) (1,0)일 때 합
# 내 위치가 (0,1)일 때 합 -> solve(0,1) (0,1)일 때 합
#...
# 내 위치가 (N-1, N-1)일 때 최소합 구하고 종료

def solve(r,c,now_sum): # r과 c 그리고 현재의 합을 인자로 함수를 구동시키겠다.
    global min_sum

    # 종료조건
    if (r,c) == (N-1, N-1): # 함수가 맨 우측 하단에 가면 종료된다.
        min_sum = min(now_sum, min_sum) # 최소합은 현재영역에서 합과 최소합에서 젤 작은거 넣는다.
        return
    
    # 재귀호출 -> 다음위치로 이동 
    for d in range(2): # 우/하 이동한다.
        nr = r + dr[d]
        nc = c + dc[d]
        if is_valid(nr,nc): # 새로운 nr,nc가 자판안에 있는지 확인하고
            solve(nr,nc,now_sum+arr[nr][nc]) # nr,nc를 현위치로하여 이동한다.
            # 바로 위 solve가 영향을 미치는 것은?
            # 일단 없다
            # 만약 이렇게 작성했다면
        if is_valid(nr,nc):
            now_sum += arr[nr][nc]
            # 
            solve(nr,nc, now_sum)
            # 여기서 방금 위의 arr[nr][nc]를 제거해주지 않으면
            # 이번것의 [nr][nc]가 더해진 것들이 ..
            # 옆의 함수에 영향을 끼칠 수 있다.


for tc in range(1, T + 1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    min_sum = 9999999


    solve(0, 0, arr[0][0])
    print(f"#{tc} {min_sum}")



# 최소합 반복문
    #(r,c)까지 오는데 최소 합은 위 또는 왼쪽 둘중에 작은 것 
    # 중간위치(r,c)까지의 합을 다시 계산하지 않도록 저장
    arr_sum = [[0]*n for_ in range(n)]

    for r in range(N):
        for c in range(N):
            # r,c 위치에서 위에서, 왼쪽에서 올 수 있을 때
            if r-1>=0 and c-1 >=0:
                # arr_sum[r][c]는 왼쪽, 위쪽에서 올 수 있는 값중 작은 것 + arr[r][c]다
                arr_sum[r][c] = min(arr_sum[r-1][c], arr[r][c-1])+ arr[r][c] 
            elif r-1>=0 and c-1<0:
                # 위쪽에서만 올 수 있다.
                arr_sum[r][c] = arr_sum[r-1] + arr[r][c]
                # 왼쪽에서만 올 수 있다.
            elif r-1<0 and c-1>=0:
                arr_sum[r][c] = arr_sum[r][c-1] + arr[r][c]
            elif r-1 <0 and c-1<0:
                arr_sum[r][c] = arr[r][c]
            

    


