
def baby_gin(idx, used, lst):
    if idx == 6:
        print(used)
        front = [list[i] for i in used[:3]]
        rear = [list[i] for i in used[:3]]

    for i in range(6):
        if i not in used:
            used.append(i)
            baby_gin(idx+1, used, lst)
            used.pop()

baby_gin(0, [], [1,2,4,7,8,3])         


for i in range(6):
    for i not in used:
        used.append(i)
        baby_gin(idx+1, used, lst)
        used.pop()