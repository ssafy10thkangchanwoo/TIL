T = int(input())

ZER = 0
ONE = 1
TWO = 2
THR = 3
FOR = 4
FIV = 5
SIX = 6
SVN = 7
EGT = 8
NIN = 9

for i in range(1, T+1):
    N = int(input())
    arr = int(input().split())
    cnt = 0
    vacant = [0]*10
    for i in range(N):
        for j in range(10):
            if arr[i] == j:
                cnt += 1

            vacant[j] = cnt

    for n in range(1, 10):
        vacant[n] += vacant[n-1]

    for k in range()









