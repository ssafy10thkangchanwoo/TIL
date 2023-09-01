
def patrol(now, e_sum):
    global min_v
 
    # 가지치기 # 있으면 좀 더 빨라짐
    if e_sum > min_v:
        return 
    
    # 종료조건
    # 모든 방을 다 방문했으면 시작지점으로 돌아가는 양까지 계산
    # 최소값 구하기
    if 0 not in visited:
        min_v = min(min_v, e_sum+e[now][0])
        return 
    
    # now 위치에서 할 일
    # now 위치에서 갈 수 있는 방을 선택
    # 선택기준 => 이전에 내가 방문한 적이 없는 방
    for next_room in range(N):
        if visited[next_room] == 0 and next_room != now:
            # next_room은 갈 수 있는 방
            visited[next_room] = 1
            patrol(next_room, e_sum + e[now][next_room])
            visited[next_room] = 0

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    e = [list(map(int,input().split())) for _ in range(N)]
    # e[i][j] = i번 방에서 j번 방으로 가는데 소모하는 배터리 양
    # 방문체크
    visited = [0]*N 
    # 출발시 첫번째 방은 방문했다고 처리
    visited[0] = 1
    min_v = 9999
    patrol(0,0)

    print(f'#{tc} {min_v}')