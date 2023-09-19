import sys
sys.stdin = open('work_percent.txt')
input = sys.stdin.readline

def work(i, visited, p):
    global max_p

    if i == N:
        max_p = max(p, max_p)
        return 
    else:
        if max_p > p:
            return


    for n in range(0, N):
        if visited[n] == 0:
            visited[n] = 1
            work(i+1, visited, p*matrix[i][n]/100)
            visited[n] = 0
         

T = int(input())
for tc in range(1, T+1):
    N= int(input())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    p = 1
    max_p = 0
    visited = [0]*(N+1)
    work(0, visited, p)
    max_p = round((max_p), 7) * 100
    answer = f'{max_p:.6f}'    
    print(f'#{tc} {answer}')