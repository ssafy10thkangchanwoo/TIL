def travel(r,c,cnt):
    if (r, c) == (N-1, N-1):
         min_box.append(cnt)
         return
    else:
        for dr, dc in ((1, 0), (0, 1)):
            nr, nc = r+dr, c+dc 
            if 0<= nc < N and 0<= nr < N:
                # cnt += matrix[nr][nc]
                r = nr # 아 이거 어제 할 때 막혔던 부분임... 
                c = nc # 이렇게 쓰면 r은 변형됐는데 
                # travel(r,c,cnt) # return추가할 경우 결과 값이 바뀐 것에 대해.
                travel(r, c, cnt+matrix[nr][nc])
                # cnt -= matrix[nr][nc] # 이전 함수까지 실행한 것에 돌아가려면(복구)하려면 빼야함.
                # travel(nr, nc, cnt + matrix[nr][nc])
                    #### 또 호출해서 아래 실행됐다.
                    # def travel(r,c,cnt):
                    #     if (r, c) == (N-1, N-1):
                    #          min_box.append(cnt)
                    #          return
                    #     else:
                    #         for dr, dc in ((1, 0), (0, 1)):
                    #             nr, nc = r+dr, c+dc 
                    #             if 0<= nc < N and 0<= nr < N:
                            #           cnt += matrix[nr][nc]
                                     # r = nr # 이대로 가면 복구시(ex:-2단계시점)에도 해당 내역 남음.
                                     # c = nc # 재설정했다는 소리

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
    
