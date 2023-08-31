def nCr(n,r):
    if r == 0:
        print(tr)
    elif n<r: # 남은 원소보다 많은 원소를 선택해야 하는 경우
        return # 불가
    else:
        tr[r-1] = a[n-1] # a[n-1]번쨰 원소를 조합에 포함하는 경우
        nCr(n-1, r-1)
        nCr(n-1, r) # a[n-1]을 포함시키지 않는 경우

a = [1,2,3,4,5]
n = 5
r = 3
tr = [0]*r
nCr(n,r)