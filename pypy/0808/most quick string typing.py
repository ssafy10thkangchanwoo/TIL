T = int(input())
for tc in range(1, T+1):
    text, cheat = input().split()

    text_num = len(text)
    cheat_num = len(cheat)

    tidx = 0
    cidx = 0
    counts = 0
    answer = 0
    # tidx, cidx가 각각 text_num, cheat_num을 넘기면 안된다.
    # cidx[어디서부터 어디까지] 가 tidx[0부터 cheat_num
    while tidx < text_num and cidx < cheat_num:
        if text[tidx] != cheat[cidx]:
            tidx = tidx - cidx
            cidx = -1

        tidx += 1
        cidx += 1

        if cidx == cheat_num:
            counts += cheat_num -1
            tidx = tidx - cidx + 1
            cidx = 0

    answer = text_num - counts

    print(f'#{tc} {answer}')
