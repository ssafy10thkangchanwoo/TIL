T = int(input())
for tc in range(1, T+1):
    D, M, T, Y = map(int,input().split())
    plan = [0]+list(map(int,input().split()))
    
    # all_D = sum(plan)*D 
    # cheapest = all=D
    
    for i in range(1, 12+1):
        plan[i] = plan[i]*D 
        if plan[i] > M:
            plan[i] = M 
    
    max_v = 0
    temp= []
    for j in range(2, 11+1):
        c = plan[j-1]+plan[j]+plan[j+1]
     
        if c > T:
            temp.append([j, c])

        
        temp.sort(key=lambda x: -[x])
        
        if 

        plan[j-1] = 0
        plan[j] = 0
        plan[j+1] = 0
        plan[0] += T

    cost = sum(plan)
    if cost > Y:
        result = Y 
    else:
        result = cost
    
    print(f'#{tc} {result}')