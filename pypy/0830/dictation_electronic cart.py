# now 현재 방 번호
# e_sum 현재까지 사용한 배터리 사용량

def patrol(now, e_sum): # 현재위치와 현재위치까지 사용한 배터리 사용량을 인자로 갖겠다.
    global min_value

    if e_sum >= min_value: # 현재까지 사용량이 최소값보다 많다면 더 볼 필요가 없다.
        return

    # 종료 조건
    # 모든 방을 다 방문했으면 시작지점으로 돌아가는 배터리 양까지 계산
    # 최소값 구하기
    if 0 not in visited: # 만약 방문 안했던 곳이 없다면?
        min_value = min(min_value, e_sum + e[now][0]) # min_value는 현재까지 최소값과 현재까지의 배터리사용량+귀환요금 중 작은 값이다.

        
    for next_room in range(n):
        if visited[next_room] == 0 and next_room != now:
            # 다음 행선지를 순회하는데 만약 다음 행선지를 방문하지 않았으면 지나간다
            # 그리고 다음 행선지가 현재위치가 아니라면(필요있나? 없어보이는데)
            # 이미 현재위치에 온 시점에서 now는 visited에 기록되어 있을터다.
            visited[next_room] = 1
            # 위의 조건을 만족시키면 방문 기록을 남긴다.(방문했다는 뜻)
            patrol(next_room, e_sum+e[now][next_room])
            # 다음 함수를 시행한다. #현재 방 그리고 현재까지의 배터리사용량을 합한다.
            visited[next_room] = 0
            # 나중 함수최종종료 후 다른 쪽 함수 영향을 떨치기 위해 ?
    

for tc in range(1, T + 1):
    n = int(input()) 

    e = [list(map(int, input().split())) for _ in range(n)]
    # e[i][j] = i번방에서 j번방으로 가는데 소모하는 배터리 양

    visited = [0] * n
    # 출발시 첫번째 방은 방문했다고 처리
    visited[0] = 1

    min_value = 10000
    patrol(0, 0)
