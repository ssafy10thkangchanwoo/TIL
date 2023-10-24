# import sys 
# sys.stdin=open('input.txt', 'rt')


T = int(input())
for tc in range(1, T+1):
    N, X = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    breakcount = 0
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == matrix[i][j+1]:
                continue 
            else:
                matrix