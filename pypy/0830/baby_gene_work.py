
cards = list(map(int,input().split()))
p1 = [0]*6
p2 = [0]*6
for i in range(len(cards)):
    if i%2 == 0:
        p1[i//2] = cards[i]
    else:
        p2[i//2] = cards[i]