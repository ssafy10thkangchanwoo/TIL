dr = [0, 1]
dc = [1, 0]

# 각 부분에 대한 값은 함수의 파라미터로 받고
# 각 부분에 대한 비교값(모든 함수에서 비교할) 것 은 글로벌
def is_valid(r,c):
    return 0<= r < N and 0<= c < N

def solve(r,c,now_sum):
    global min_sum
    # 종료조건
    if (r, c) == (N-1, N-1):
        # 최소 합을 구하기
        return 
    # (r,c)에서 해야할 일
    now_sum += arr[r][c]
    # 재귀 호출 -> 다음 위치로 이동(아래 또는 오른쪽으로 이동)
    for d in range(2):
        nr = r + dr[d]
        nc = c + dc[d]
        if is_valid(nr,nc):
            solve(nr,nc,now_sum + arr[r][c])

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    arr = [list(map(int,input().split())) for _ in range(N)]

    min_sum = 9999