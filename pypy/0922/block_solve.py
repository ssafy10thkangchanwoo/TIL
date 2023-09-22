form 
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
# 내가 지금까지 공을 떨어뜨린 횟수 : n 
def pick(n):
    # n번 공을 떨어뜨림(공을 떨어뜨릴 위치를 n번 고름)
    if n== N:
        return 
    
    for c in range(W):
        # c번 열에서 공을 떨어뜨려 보기
        # 공을 한번 떨굴때마다 벽돌의 상태가 변해야 하므로
        # deepcopy해서 각 상태 유지
        now_bricks = [[bricks[i][j] for j in range(W) for i in range(H)]]
        
        # bfs로 상하좌우 터지는 것 구현
        q = deque()

        # 위에서부터 벽돌찾기
        for r in range(H):
            if now_bricks[r][c]:
            q.append((r,c, now_bricks[r][c]))       
            now_bricks[r][c] = 0 # 쾅
            break # 밑에 벽돌은 아직 터뜨리면 안돼

        # 벽돌없으면 안터뜨려도 됨, 건너뛰기
        if not q:
            continue
        # 벽돌 부수기 시작 

        # 부순 벽돌의 개수 
        b_cnt = 0 
        # BFS, 벽돌 부순다.
        while q:
            # i : 벽돌 행번호, j 벽돌 열 번호
            # k: 벽돌에 적힌 숫자(파괴 범위)

            i, j, k = q.popleft()
            b_cnt += 1 # 벽돌 하나 깨짐
            for l in range(1, k):
                for d in range(4):
                    ni = i+ dr[d]*l
                    nj = j + dc[d]*l 
                    if 0<= ni < H and 0 <= nj < W and now_bricks[ni][nj]:
                        # 벽돌에 적힌 숫자가 1보다 큰 경우에만 큐에 삽입
                        # 1이하면 안퍼져나가니까
                        if now_bricks[ni][nj]>1:
                            q.append((ni,nj, now_bricks[ni][nj]))
                        now_bricks[ni][nj] = 0 # 쾅

    # 벽돌 다 부수고 나서 빈 공간 처리
        for j in range(W):
            
            # 밑에서부터 0인 부분 찾고 거기서부터 땡겨오기
            for i in range(H-1, -1, -1):
                if not now_bricks[i][j] 
                    continue
                temp_list.append((h,w, matrix[h][w])) # 아래것일수록 늦은

            # 다시 새로운 줄을 만든다.
            for h in range(H-1, -1, -1):


        pick(n+1)
    


for tc in range(1, T+1):
    # N : 드랍횟수
    # W : 가로, H 세로

    N, W, H = map(int, input().split())

    # 벽덜정보
    bricks = [list(map(int,input().split())) for _ in range(H)]

    # 남은 벽돌의 개수의 최소값
    answer = W*H*10

    # 남은 벽돌의 개수 => 0이 되면 더 구슬을 떨어뜨릴 필요가 없음.

    remain = 0
    for r in range(H):
        for c in range(W):
            if bricks[r][c]:
                remain += 1

    # 재귀 함수


