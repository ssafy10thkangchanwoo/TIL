def travel(r,c,cnt):
    if (r, c) == (N-1, N-1):
         min_box.append(cnt)
         return
    else:
        for dr, dc in ((1, 0), (0, 1)):
            nr, nc = r+dr, c+dc 
            if 0<= nc < N and 0<= nr < N:
                # cnt += matrix[nr][nc]
                # r = nr # 아 이거 어제 할 때 막혔던 부분임... 이전경로 고장
                # c = nc
                # travel(r,c,cnt) # return추가할 경우 결과 값이 바뀐 것에 대해.
                return travel(nr, nc, cnt+matrix[nr][nc])
                # cnt -= matrix[nr][nc]

                # travel(nr, nc, cnt + matrix[nr][nc])
                

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    r, c = 0, 0
    min_box = []
    cnt = matrix[r][c]
    travel(r,c,cnt)
    min_v = min(min_box)
    print(f'#{tc} {min_v}')
    
