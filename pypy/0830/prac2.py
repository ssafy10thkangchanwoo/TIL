def generate(numRows):
    res = [[1]]

    for i in range(numRows -1):
        temp = [0] + res[-1] + [0]
        row = []
        for j in range(len(res[-1]) +1):
            row.append(temp[j] + temp[j+1])
        res.append(row)
    return res

print(generate(5))


def tri(n, tower):
    temp = [0]+ tower[-1] + [0]
    new = []
    for j in range(len(res[-1]) +1):
        new.append(temp[j]+)