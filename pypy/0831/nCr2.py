def nCr(n,r, s):
    if r == 0:
        print(*comb)
    else:
        for i in range(s, n-r+1):
            comb[r-1] = A[i]
            nCr(n, r-1, i+1)

 # n과 r이 케이스마다 다른데? -> 재귀 사용
A = [1,2,3,4,5]
n = 5
r = 3
comb = [0]*r
nCr(n,r, 0)