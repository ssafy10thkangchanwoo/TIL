T = int(input())

def recur(level, acc_height):
    global ans

    # 가지치기
    # 현재까지 탑이 선반 높이를 넘어간다면
    # 앞으로 더 볼 필요가 없다.
    if acc_height >= B:
        ans = min(ans, acc_height)


    # 기저 조건
    if level==N:
        return

    # 해당점원을 탑에 쓸 경우
    recur(level+1, acc_height + arr[level])
    # 안 쓸 경우
    recur(level+1, acc_height)
    # 들어가기 전(가지치기)

    # 돌아왔을 때


for tc in range(1, T+1):
    N,B = map(int,input().split())
    arr = list(map(int,input().split()))
    # 백트랙킹
    # 차이의 최소
    ans = int(1e9) # 대충 엄청 큰 숫자
    recur(0, 0)
    print(f'#{tc} {ans-B}')