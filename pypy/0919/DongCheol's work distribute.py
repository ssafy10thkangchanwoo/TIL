import sys
sys.stdin = open('work_percent.txt')
input = sys.stdin.readline

def work(i, visited, p):
    global max_p

    if i == N:
        max_p = max(p, max_p)
        return 
  	# 가지치기1. max_p(N번째까지 다 곱한 값)이 p(N번째까지 곱하지 않는 것 포함)보다 크면 끊어냄
    if max_p >= p:
        return
    # 가지치기 2. 현재 p에서 남은 확률 값(미래에 곱할 값) 중에서 최대치를 모두 곱했는데도 max_p가 더 크다면 가지치기
    temp_p = p
    for j in range(i, N):
        temp_p *= max(matrix[j])/100
    if temp_p <= max_p:
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
    # 소수점 차이 줄이기/ 큰 수를 다루는 것이 오차가 적다
    # max_p = round((max_p), 7) * 100
    max_p = round(max_p*100, 7) 
    answer = f'{max_p:.6f}'    
    print(f'#{tc} {answer}')