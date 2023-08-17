numbers = [1, 2, 3]
n = len(numbers)

def perm1(i):
    if i == n:
        print(numbers)
        return
    for j in range(i, n):
        numbers[i], numbers[j] = numbers[j],numbers[i]

        perm1(i+1)

        numbers[i], numbers[j] = numbers[j], numbers[i] # 원상복구

perm1(0)

