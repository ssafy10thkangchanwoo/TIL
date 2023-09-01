T = int(input())
for tc in range(1, T+1):
    bi = input()
    tr = list(int(input()))

    N = len(bi)
    M = len(tr)

    binary = int(bi,2)
    bin_list = [0]*N
    tri_list = [0]*M

    for i in range(N):
        bin_list[i] = binary ^ (1<<i) # binary의 숫자와 비트를 i번 이동시킨 것과 다르면 1을 반환
        # bin_list에는 1자리마다 반대값들이 저장되어 있을 것이다.
        # 나중에 bin_list는 bi 값과 한자리씩 교체하기 위해 쓰이나요?

    for i in range(M):
        num1 = 0
        num2 = 0
        for j in range(M):
            if i != j:
                num1 = num1*3 + tr[j]
                num2 = num2*3 + tr[j]

            else:
                num1 = num1 * 3 + (tr[j]+1)%3
                num2 = num2 * 3 + (tr[j]+2)%3

    if num1 in bin_list:

