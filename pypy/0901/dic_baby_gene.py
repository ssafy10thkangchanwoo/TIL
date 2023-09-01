def is_run(p):
    return p[0] == p[1]-1 and p[1]==p[2] -1

def is_triple(p):
    return p[0] == p[1] and p[1] == p[2]

def perm(idx, selected, n, deck, player): 
    global winner
    if idx == 3:
        p = [deck[i] for i in selected]
        
        if is_triple(p) or is_run(p):
            winner = player

    
    for i in range(n):
        if i not in selected:
            selected.append(i)
            perm(idx + 1, selected, n, deck, player)
            selected.pop()

for tc in range(1, T + 1):
    cards = list(map(int, input().split()))  # 카드 정보
    
    turn = 0

    A = []
    B = []

    winner = -1 

    while turn<6:
        A.append(cards[turn*2])
        B.append(cards[turn*2+1])

        if turn >= 2:
            perm(0, [], len(A), A, 1)
            
            if winner != -1:
                break

            perm(0,[],len(B),B,2)

            if winner != -1:
                break
            
        turn += 1
    
    if winner == -1:
        winnder = 0
