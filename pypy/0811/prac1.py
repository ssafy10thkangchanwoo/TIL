T = 10

def dfs(s):
    # 방문 배열 만들기
    visited = [0]*100
    # 스택
    stack = []
    s= 0 # 시작점
    # 시작 정점은 방문 처리
    visited[s] = 1
    # 현재 정점 번호를 i라고 하자
    i = s
    # 모든 정점을 방문할 때까지 처리
    while True:
        # 현재 정점 i가 도착지점인지 확인
        if i == 99:
            # 도착지점이니까 반복 종료
            # 반복문 뿐만 아니라 함수를 더이상 실행할 필요도 없다.
            return 1
        # 방문위치 i에서 방문할 수 있는 정점 j를 확인하고
        # 방문 가능하면 방문
        for j in range(100):
            # i정점에서 j정점으로 가는 길이 있고
            # j정점을 방문한 적이 없으면 ㄱㄱ
            if adj[i][j] == 1 and not visited[j]:
                # j를 방문처리
                visited[j] = 1
                # 돌아올 위치(현재위치)기억
                stack.append(i)
                # 다음 위치로 이동
                i = j
                # 이전 위치로의 탐색을 중단
                break
        else:
            # 현재 위치 i에서 방문할 수 있는 j가 없었다.
            if stack:
                # 제일 최근에 방문했던 정점으로 돌아가기
                i = stack.pop()
            else:
                # 스택이 비어있다 ==> 갈 수 있는 정점은 모두 방문했다.
                break

    # 여기까지 코드가 실행되었다.
    # 반복이 끝났으니까 내가 갈 수 있는 정점은 모두 방문한 상태
        return 0

for tc in range(1, T+1):
    # 간선의 개수
    _, E= map(int, input().split())

    # 순서쌍을 배열로 받기
    edges = list(map(int,input().split()))

    # 인접행렬
    adj =[[0]*100 for _ in range(100)]
    # adj[i][j] ==> i정점에서 j정점으로 가는 길이 있는지 표현
    # 순서쌍을 통해 인접행렬 만들기

    for i in range(E):
        # 간선의 개수 * 2 = 정점의 개수
        adj[edges[i*2]]= edges[i*2+1]

    print(f"{tc} {dfs(0)}")
