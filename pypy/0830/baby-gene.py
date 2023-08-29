def baby_gene(numbers):
    if cnt == 2:
        return 'babygene'
    for i in range(2):
        if numbers[3*i+2]-numbers[3*i+1] and numbers[3*i+1]-numbers[3*i+0]:
            cnt += 1
        if numbers[3*i+0] == numbers[3*i+1] == numbers[3*i+2]:
            cnt += 1

def perm(i, 6):
    if i == 6:
        print(p)
    else:
        for j in range(6):
            if used[j] == 0:
                p[i] = numbers[j]
                used[j] = 1
                perm(i+1, 6)
                used[j] = 0

# # idx에 놓을 숫자 찾아서 놓기
# def baby_gin(idx, used, lst):
#     # 종료조건:6개 숫자 자리를 다 정해줌
#     if idx == 6:
#         # 베이비진 검사
#         앞 = [lst[i] for i in used[:3]]
#         뒤 = [lst[i] for i in used[3:]]
#         return 
    
#     # 6개 숫자중에 하나 골라서 idx위치에 놓기(이전에 고른거 빼고)
#     for i in range(6):
#         if i not in used:
#             used.appent(i)
#             baby_gin(idx+1, used, lst)
#             used.pop()

        
numbers = list(map(int,input()))
used = [0] * 6
p = [] * 6





