num = 456789
c = [0]*12

for i in range(6):
    c[num%10] += 1
    num //= 10

i = 0
tri = num = 0
while i < 10:
    if c[i] >= 3:
        c[i] -= 3
        tri += 1
        continue

        if c[i] >= 1 and