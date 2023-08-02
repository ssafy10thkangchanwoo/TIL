T = 10
for tc in range(1, T+1):
    N = int(input()) # 건물의 개수
    # 각 건물의 높이가 담긴 리스트(배열)
    # input()함수는 한줄씩 읽는다.
    # split()함수를 쓰면 문자열을 " " 기준으로 자른다.
    # 각 문자열 조각을 숫자로 바꾸는 작업도 진행 해야 한다.
    # 반복문을 통해서 일일이 다 int를 적용해도 된다.
    # map()함수를 쓰면 반복문 필요 X
    # map(적용할 함수, 적용할 리스트(컨테이너))
    # 우리가 적용할 함수는 int, 적용할 리스트는 입력되 문자열을 ""기준으로 쪼갠 배열
    # map(int, input().split())
    # map 함수의 결과는 리스트가 아니기 떄문에 우리가 쓰기 편한 리스트로 바꾼다.
    buildings = list(map(int,input().split()))

    # 조망권을 가지는 세대 수
    count = 0

    # 반복문을 통해서 각 빌딩의 조망권이 확보된 세대의 개수를 세준다.

    # 중첩 반복문 활용
    # 한 빌딩의 모든 세대를 다 확인하고 다음 빌딩으로 넘어갈 것이기 때문에
    # 밖의 반복문은 빌딩의 개수를 세는데 쓰겠다.
    # 안의 반복문은 빌딩의 층수를 세는데 쓰겠다.
    for i in range(2, N-2): #양쪽 2칸씩은 무조건 높이가 0 => 확인할 필요 없음.
        height = buildings[i]
        for j in range(height, -1, -1): # 시작 = 꼭대기, 끝 = 0, -1
            # 현재 i번째 건물 층수 j
            # j층에서 양쪽 2칸을 확인한다면 조망권이 있으면 count를 1씩 증가
            # 왼쪽 -1, -2 건물 높이 확인, 오른쪽 +1, +2 건물의 높이 확인
            # 현재 j층이 왼쪽과 오른쪽 건물의 높이보다 높아야 조망권 OK.
            # 왼쪽 -1 => buildings[i-1], i-2, i+1, i+2
            if j > buildings[i-1] and j > buildings[i-2] and j > buildings[i+1] and j > buildings[i+2]:
                count += 1
            else:
                # 조망권이 없는 밑층은 확인할 필요가 없다.
                break

    print(f"#{tc} {count}")
