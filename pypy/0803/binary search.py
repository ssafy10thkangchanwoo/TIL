T = int(input())

for tc in range(1, T+1):
    p, a, b = map(int,(input().split()))
    count_a = 0
    count_b = 0
    start_p = 1
    end_p = p
    winner = 0
    while start_p <= end_p:
        if (start_p+end_p)//2 == a:
            count_a += 1
            break
        elif (start_p+end_p)//2 > a:
            count_a += 1
            end_p = (start_p+end_p)//2
        else: 
            count_a += 1
            start_p = (start_p+end_p)//2


    start_p = 1
    end_p = p
    while start_p <= end_p:
        if (start_p+end_p)//2 == b:
            count_b += 1
            break
        elif (start_p+end_p)//2 > b:
            count_b += 1
            end_p = (start_p+end_p)//2
        else: 
            count_b += 1
            start_p = (start_p+end_p)//2
    
    if count_a > count_b:
        winner = "B"
    elif count_a < count_b:
        winner = "A"
    else: 
        winner = "0"

    print(f'#{tc} {winner}')




    