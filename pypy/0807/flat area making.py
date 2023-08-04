# 테스트 캐이수 갯수
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # 평탄화 영역 설정
    r1, c1, r2, c2 = map(int, input().split())
    # N*N 매트릭스 생성
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 1 평균을 구하기 위해서는 총합, 영억의 칸수를 알아야 한다.
    sumV = 0 # 총합
    cnt = 0 # 영역의 갯수

    for r in range(r1, r2+1):
        for c in range(c1, c2+1):
            sumV += arr[r][c]
            cnt += 1

    # 2. 평균값 구하기
    avgV = sumV // cnt

    # 총 작업 횟수
    result = 0

    # 3  작업 횟수를 센다.
    for r in range(r1, r2+1):
        for c in range(c1, c2+1):
            # 작업 횟수를 구하는 방법
            # 현재 (r,c) 위치의 높이 : 평균값의 절대값
            sub = arr[r][c] - avgV
            if sub < 0:
                sub =-sub
            result += sub

    print(f'#{tc} {result}')
