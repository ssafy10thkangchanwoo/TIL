T = int(input())

for tc in (1, T+1):
    pattern = input()
    text = input()

    pidx = 0
    tidx = 0

    answer = 0

    while tidx < len(text) and pidx<len(pattern):
        if pattern[pidx] == text[tidx]:
            pidx += 1
            tidx += 1

        else:
            tidx = tidx -pidx +1 # 여기 생각하는데 좀 난이도 있어보이는데데
           pidx = 0

    if pidx == len(pattern):
        answer = 1
        break