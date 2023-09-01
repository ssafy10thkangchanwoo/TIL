T = int(input())

for tc in range(1, T+1):
    bi = input()
    tr = list(int(input()))
    
    N = len(bi)
    M = len(tr)

    binary = int(bi, 2) # 2진수형태의 문자열을 10진법정수형태로 나타내봐
    bin_list = [0]*N
    tri_list = [0]*M
    ans = 0
    for i in range(N): # 각 비트를 반전시킨 2진수 만들기.
        bin_list[i] = binary ^ (1<<i) # exclusivOr

    for i in range(M): # 3진수의 tr[i]자리를 바꾼 숫자 만들기
        num1 = 0  # (tr[i]+1)%3
        num2 = 0  # (tr[i]+2)%3
        for j in range(M):
            if i != j:
                num1 = num1*3 + tr[j]
                num2 = num2*3 + tr[j]
            else:
                num1 = num1*3 + (tr[j]+1)%3
                num2 = num2*3 + (tr[j]+2)%3
    if num1 in bin_list:
        ans = num1 
        break # for i를 중단한다고?
    if num2 in bin_list:
        ans = num2
        break

    print(bin_list)    


    