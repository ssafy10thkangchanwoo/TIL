def is_run(p):
    return p[0] == p[1] -1 and p[1] == p[2] -1

def is_triplet(p):
    return p[0] == p[1] == p[2]



def perm(idx, selected, n, deck, player):
    global winner

    # run이나 triplet확인하고 승자를 결정
    if idx == 3:
        p = [deck[i] for i in selected] # 순열 만들기
        # p가 run인지 triplet인지?
        if is_triplet(p) or is_run(p):
            winner = player
        return
    
    # 카드를 고를 수 있는 경우의 수는 
    for i in range(n):
        # i 번째 카드를 뽑아서 순열 만들건데 전에 고른적이 없어야 한다.
        if i not in selected:
            # i 번째 카드를 고르고 idx+1번째 카드를 고르러 간다.
            selected.append(i)
            # 다음 카드를 고르러 간다.
            perm(idx+1, selected, n, deck, player)
            # i번째 카드를 고르지 않았다고 치고 다시 원상복구
            selected.pop()

T = int(input())
for tc in range(1, T+1):
    cards = list(map(int,input().split())) # 카드 정보

    # 카드 가져가는 순서
    turn = 0
    
    A = [] # 1번 플레이어의 카드 정보
    B = [] # 2번 플레이어의 카드 정보
    # 누가 이겼는가?
    winner = -1
    
    while turn<6:
        A.append(cards[turn*2])
        B.append(cards[turn*2+1])

        if turn >= 3:

        # 1번 플레이어가 baby gin이 되는지 판단
        # 1번 플레이어가 가진 카드중에 3개 뽑아서 순열만들기
        # 1번 플레이어가 run이나 triplet이면 승자는 1번
            perm(0, [], len(A), A, 1)
            # 승자가 정해지면 더 이상 진행하 필요 X
            if winner != -1:
                break

        # 2번 플레이어가 baby gin이 되는지 판단
        # 2번 플레이어가 가진 카드중에 3개 뽑아서 순열 만들기
        # 2번 플레이어가 run이나 triplet이면 승자는 2번
            perm(0, [], len(B), B, 1)
            # 승자가 정해지면 더 이상 진행하 필요 X
            if winner != -1:
                break
            
        turn += 1
         
    # 카드 6장씩 다 나눠줬는데 승자가 없어
    if winner == -1:
        winner = 0
        