T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int,input().split()))
    num_set = [[] for _ in range(N)]
    for n in numbers:
        for i in range(1,n):
            if n%i == 0:
                num_set[n-1].append(i)
    
    print(num_set)


n=1000
a = [False,False] + [True]*(n-1)
primes=[]

for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False
print(primes)
