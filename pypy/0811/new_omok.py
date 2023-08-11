T = int(input())
# 델타배열
# 대각선 포함이라서 8방향 다 봐야할 것 같지만
# 4방향만 봐도 된다.
# 오른쪽 아래 == 왼쪽위 // 우==좌 // 상== 하 // 오른쪽 위==왼쪽아래
dr = [0,1,1,1]
dc = [1,1,0,-1]

# (r,c)가 유효한 위치인지 검사하는 함수
def is_valid(r,c):
    return 0<= r < N and 0<= c <= N

def solve():
    # 모든 위치(r,c)에서 내가 돌을 발견하면
    # 그 돌과 연결된 돌들이 5개 있는지 확인
    # 5개 있으면 Yes
    # 하나도 발견 못하면 No

    for r in range(N):
        for c in range(N):
            # (r,c)에서 돌을 발견했다.
            if arr[r][c] == "o":
                # 4방향으로 탐색(이어진 돌의 개수 세기)
                for d in range(4):
                    # 오목이니까 한방향당 5칸씩 가보자.
                    for k in range(5):
                        nr = r + dr[d]*k
                        nc = c + dc[d]*k
                        # 다음 위치 계산했는데 돌이 아니거나 범위 밖이면 중단
                        if not is_valid(nr,nc) or arr[nr][nc] == '.':
                            break
                    else:
                        # 5번 반복했는데 중간에 break가 없었다.
                        return 'YES'
    # 함수가 여기까지 실행된 경우
    # 오목을 찾지 못함.
    return "NO"

for tc in range(1, T+1):
    N = int(input())

    # 바둑판
    arr = [list(input()) for _ in range(N)]

    # 정답 출력
    print(f'#{tc} {solve()}')


