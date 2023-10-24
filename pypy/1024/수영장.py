T = int(input())
for tc in range(1, T+1):
    # 기간별 이용권 가격리스트
    D, M, TR, Y = map(int,input().split())
    # 각 월별 이용 계획
    plan = [0]+list(map(int,input().split()))
    
    # all_D = sum(plan)*D 
    # cheapest = all=D
    
    for i in range(1, 12+1):
        plan[i] = plan[i]*D 
        if plan[i] > M:
            plan[i] = M 
    
    max_v = 0
    temp = []
    for j in range(2, 11+1):
        c = plan[j-1] + plan[j] + plan[j+1]
        if c > TR:
            temp.append([j, c])

    temp.sort(key=lambda x: -x[1])

    used_months = set()

    while temp:
        j, c = temp[0]  # 가장 비용이 높은 월 선택
        if j-1 not in used_months and j not in used_months and j+1 not in used_months:
            plan[j-1] = 0
            plan[j] = 0
            plan[j+1] = 0
            plan[0] += TR

            # 사용한 월들 추가
            used_months.update([j-1, j, j+1])
        
        # 이미 사용한 월이 포함된 항목 제거
        temp = [item for item in temp if item[0]-1 not in used_months and item[0] not in used_months and item[0]+1 not in used_months]

    cost = sum(plan)
    if cost > Y:
        result = Y 
    else:
        result = cost
    
    print(f'#{tc} {result}')