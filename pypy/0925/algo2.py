T = int(input())
# r: 내가 현재 r번째 행에서 몇번째 열에 있는 과녁을 맞출 것인가?
# selected : 내가 이전에 골랐던 열은 다시 고르지 않도록 체크
# score : 내가 지금까지 맞춘 점수
def shoot(r, selected, score):
    global max_score
    # 종료
    if r == N:
        max_score = max(score,max_score)
        return 
    # 재귀 호출
    for c in range(N):
        if not selected[c]:
            selected[c] = 1
            shoot(r+1, selected, score+arr[r][c])
            selected[c] = 0

for tc in range(1, T+1):
    N = int(input())

    arr =[list(map(int,input().split())) for _ in range(N)]

    # 최대점수
    max_score = 0

    shoot(0, [0]*N, 0)
    print(f'#{tc} {max_score}')