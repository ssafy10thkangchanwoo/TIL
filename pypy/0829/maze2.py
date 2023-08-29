import sys
sys.stdin = open('maze.txt','r')
T = 10
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def start(maze):
    for r in range(100):
        for c in range(100):
            if maze[r][c] == '2':
                return (r,c)

def end(maze):
    for r in range(100):
        for c in range(100):
            if maze[r][c] == '3':
                return (r,c)

def dfs(r, c, maze, visited, stack):
    visited.append((r,c))
    stack.append((r,c))
    while stack:
        if maze[r][c] == '3':
            return '1'
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d] # 새 경로 설정하고
            # 숫자와 비교하지마.. 오타 (nr,nc)도..
            if 0<= nr <100 and 0<=nc<100 and maze[nr][nc] != '1' and (nr,nc) not in visited:
                # 갈 수 있는지 확인, 방문했던 길인지 확인
                r = nr
                c = nc
                #방문
                visited.append((r,c))
                stack.append((r,c))
                # 방문기록 남김
                break # for문에서 이번에 갔던 d번째 선택지는 택하지 못하므로 아예 초기화 함.
        else: # for문의 4방탐색 후 갈 곳이 없다면
            if stack: # 뒷걸음질 칠 곳이 잇나?
                r, c = stack.pop()#최근 방문지로 귀환, 방문기록은 삭제된다
                #근데 방문 기록 삭제되면 분기점에서 같은 선택 반복하는거 아님?

            else: # 방문기록이 없다. 가능성을 다 소진했다.
                return '0'


for tc in range(1, T+1):
    maze = [list(input()) for _ in range(100)] # 정수형으로 저장하면 하나씩 떼서 못씀.
    sr, sc = start(maze)
    er, ec = end(maze)
    visited = []
    stack = []
    print(f'#{tc} {dfs(sr,sc,maze,visited,stack)}')
