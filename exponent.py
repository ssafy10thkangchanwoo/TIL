def f1(b, e):
    global c1
    

    if b == 0:
        return 1
    r = 1
    for i in range(e):
        r *= b
        c1 +=1
    return r

def f2(b,e):
    global c2
    
    if b ==0 or e == 0:
        return 1
    
    if e%2: # 홀수
        r = f2(b, (e-1)//2)
        c2 +=1
        return r*r*b
        
    else: # 짝수면
        r = f2(b, e//2)
        c2 +=1
        return r*r
    

c1 = 0
c2 = 0

print(f1(2, 20), c1)
print(f2(2, 20), c2)
