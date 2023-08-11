i = 2
N = 5
for i in range(N):
    counts = 0
    for k in range(N - i - 1, -1, -1):
        print(k)