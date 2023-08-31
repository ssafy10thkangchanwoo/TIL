N = 10
a = [1, 4, 1, 6, 6, 10, 5, 7,3, 8, 5, 8, 3, 5, 8, 11, 2, 13, 12, 14]
meet = [] 
for i in range(N):
    meet.append([a[i*2], a[i*2+1]]) # mmet에 일단 시간대 집어 넣고
print(meet)
meet.sort(key=lambda x:x[1]) # meet에 있는 원소를 시작시간 기준으로 정렬하고
print(meet)
meet = [[0,0]] + meet # 0,0넣고
print(meet)
S =[] # 이건 뭐꼬
j = 0 
for i in range(1, N+1): # 1부터 N-1까지
    if meet[i][0] >= meet[j][1]:# si>=fj # 
        S.append(i)
        j = i
print(S)