T = int(input())
for tc in range(1, T+1):

    def comb(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 3

        else:
            return comb(n-1)+comb(n-2)

    print(comb(4))