T = int(input())
N = 0
S = 1
def rotate(o_g, o_d):
    g = o_g
    d = o_d
    l = g-1
    r = g + 1

    rotate_list = [(g,d)]

    while l >= 0:
        if gears[g][6] != gears[l][2]:
            rotate_list.append((l, -d))
        else:
            break
        g -= 1
        l -= 1
        d = -d

    g = o_g
    d = o_d

    while r < 4:
        if gears[g][2] != gears[r][6]:
            rotate_list.append((r, -d))
        else:
            break
        d = -d
        g += 1
        r += 1

    for gi, di in rotate_list:
        if di == 1:
            gears[gi] = [gears[gi].pop()] + gears[gi]
        else:
            gears[gi] = gears[gi][1:] + [gears[gi].pop(0)]


for tc in range(1, T+1):
    K = int(input())
    gears = [list(map(int,input().split())) for _ in range(4)]

    for i in range(K):
        g, d = map(int, input().split())
        g -= 1
        rotate(g, d)


