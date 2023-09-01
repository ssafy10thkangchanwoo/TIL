T = int(input())
N = 0
S = 1

def rotate(o_g,o_d): # o_g, 최초 자석 번호
    g = o_g
    d = o_d
    l = g-1
    r = g+1
    rotate_list = [(g,d)] # g번 자석을 d 방향으로 회전하겠다.
    # g기준으로 왼쪽 자석 돌리기
    # 왼쪽에 자석이 있다.
    # g번 자석의 6번 날과 l번 자석의 2번 날 비교해서 다르면 왼쪽 자석 회전
    while l>=0:
        if gears[g][6] != gears[l][2]:
            rotate_list.append((l,-d))
        else:
            break
        g -=1
        l -= 1
        d = -d

    g = o_g
    d = o_d
    # 오른쪽을 비교할 때는 g번자석의 2번 날과 r번 자석의 6번 날을 비교해서 다르면 회전
    while r<4:
        if gears[g][2] != gears[r][6]:
            rotate_list.append((r, -d))
        else:
            break
        g -=1
        l -= 1
        d = -d


    # 회전할거 리스트에서 하나씩 꺼내서 회전
    for gi, di in rotate_list:
        # gi: 회전할 자석 번호, di: 회전 방향
        if di == 1: # 오른쪽
            gears[gi] = [gears[gi].pop()] + gears[gi]
        else: #왼쪽 회전
            gears[gi] = gears[gi][1:] + gears[gi].pop(0)]

for tc in range(1, T+1):
    K = int(input())

    gears = [list(map(int,input().split())) for _ in range(4)]
    for i in range(K):
        g, d = map(int,input().split()) # g : 톱니바퀴, # d : 회전 방향
        g -= 1
        rotate(g, d)

    score = 0
    for i in range(4):
        if gears[i][0] == S:
