def f(i, j, bw, N):
    board[i][j] = bw # 돌 놓기
    for di, dj in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        ni, nj = i+di, j+dj
        temp = []
        while 0<=ni<N and 0<=nj<N and board[ni][nj]==op[bw]: # 보드 내부이고 반대색이면 계속 이동
            temp.append((ni, nj))
            ni, nj = ni+di, nj+dj
        if  0<=ni<N and 0<=nj<N and board[ni][nj]==op[bw]: # 보드내이고 같은 색이면
            for p, q in temp:
                board[p][q] = bw
B = 1 # 흑돌 1
W = 2 # 백돌 2
op = [0, 2, 1]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split()) # N: 보드 크기, M: 돌을 놓는 횟수
    play = [list(map(int, input().split())) for _ in range(M)]
    board = [[0]*N for _ in range(N)] # 0에서부터 N-1까지 인덱스 사용
    
    #중심부 4개의 돌 배치
    board[N//2-1][N//2-1] = W
    board[N//2-1][N//2] = B
    board[N//2][N//2-1] = B
    board[N//2][N//2] = W

    # 입력이 col, row, color 순으로 주어지는데
    for col, row , bw in play:
        f(row-1, col-1, bw, N):

    # 각 테스트케이스마다 게임이 끝난 후 보드 위의 흑돌, 백돌의 개수를 출력한다.
    bcnt = wcnt = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == B:
                bcnt += 1
            elif board[i][j] == W:
    print(f"#{tc} {bcnt} {wcnt}")
    
