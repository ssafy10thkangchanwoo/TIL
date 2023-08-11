T = 10
for tc in range(1, T+1):
    # 테스트케이스, 길 갯수 입력
    N, E = map(int,input().split())
    # 길 갯수개의 시작점,끝점 입력

    gil = [[]for _ in range(100)]

    #숫자쪼개기
    numbers = list(map(int, input().split()))

    for n in range(E):
        s, e = numbers[2*n], numbers[2*n-1]
        gil[s] = e

    def tracking():
        visited = []*100
        stack = []
        i = 0
        visited[i] = 1
        answer = 0
        while True:
            if i == 99:
                answer = 1
                break
            for j in gil[i]:
                if visited[j] == 0:
                    stack.append(j)
                    i = j
                    visited[j] = 1
                    break
            else:
                if stack:
                    i = stack.pop()
                else:
                    break
tracking()



T = 10
for tc in range(1, T+1):
    # 테스트케이스, 길 갯수 입력
    N, E = map(int,input().split())
    # 길 갯수개의 시작점,끝점 입력

    gil = [[]for _ in range(E)]

    #숫자쪼개기
    numbers = list(map(int, input().split()))

    for n in range(E):
        s, e = numbers[2*n], numbers[2*n+1]
        gil[s].append(e)
        
    def tracking():
        visited = [0]*100
        stack = []
        i = 0
        visited[i] = 1
        global answer
        answer = 0
        while True:
            if i == 99:
                answer = 1
                break
            for j in gil[i]:
                if visited[j] == 0:
                    stack.append(i)
                    i = j
                    visited[j] = 1
                    break
            else:
                if stack:
                    i = stack.pop()
                else:
                    break   

    tracking()
    print(f'#{tc} {answer}')
