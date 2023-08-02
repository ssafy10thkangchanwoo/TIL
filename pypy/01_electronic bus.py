# T = int(input())
# K, N, M = list(map(int, input().split()))
#
#
# for tc in range(1, T+1):
#     Nnum = list(map(int, input().split()))
#     print([0] + Nnum)
#     oil_tank = K
#     count = 0
#     for n in range(N):
#         if n in Nnum:
#             if K < Nnum[n+1] - Nnum[n]:
#                 count += 1
#                 oil_tank = K
#         if oil_tank < Nnum[n+1] - n:
#             print(0)
#         oil_tank -= 1
#
#     print(f'#{tc} {count}')

# new *
def drive(K, N):
    # return == 0 : 충전소가 제대로 배치되어 있지 않다.
    # return >0: 충전소가 배치되어 있다.
    # 한번에 갈 수 있는 K까지 가보고
    # 충전기가 없으면 다시 앞으로 한 칸씩 되돌아 오면서
    # 충전기가 있나 확인.
    # 이동하기 전 위치로 되돌아오면서 충전기를 발견하지 못했다?
    # ==> return 0

    # 되돌아오다가 충전소를 찾으면 K만큼 또 가고...<반복>
    last = 0  # 버스가 마지막으로 충전했던 위치
    next = K  # 버스가 최대로 이동한 위치(초기값은 한번 이동한 상태)
    count = 0  # 충전한 횟수

    # 반복하면서 종점까지 이동
    # 버스가 종점에 도착할 때까지 계속 반복
    while next < N:
        # 버스가 이동한 위치에 충전기가 있나 없나 검사
        while stop[next] == 0:
            # 충전기가 없으면 충전기가 나올 때까지 앞으로 되돌아오기
            next -= 1
            # 되돌아왔는데 이동하기 전 위치로 왔다면
            # 충전기의 위치가 잘못된 것이다.
            if next == last:
                return 0

        # 충전기가 제대로 설치되어 있다면
        # 마지막 충전위치를 갱신하고 다음 위치로 이동
        last = next
        next += K
        # 충전기 만났으니까 충전
        count += 1
    # 여기는 while문이 끝나야 도착할 수 있는 코드
    # 정상적으로 충전기가 배치되어 있다.
    # 충전 횟수 return
    return count


T = int(input())

for tc in range(1, T + 1):
    K, N, M = map(int, input().split())
    # K : 이동할 수 있는 거리
    # N : 버스가 가야할 거리
    # M : 충전기의 개수

    charge = list(map(int, input().split()))  # 충전기 위치 정보
    stop = [0] * N  # 정류장 리스트
    # stop[i] == 1 : 충전소가 있는 정류장
    # stop[0] == 0 : 충전소가 없는 정류장

    for x in charge:
        stop[x] = 1  # 위치 x에는 충전소가 있다.

    answer = drive(K, N)
    print(f"#{tc} {answer}")