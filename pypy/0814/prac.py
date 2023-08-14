
def check(line):
    stack = [0] * 100
    top = -1
    for c in line:
        if c in ['(' , '{']:
            top += 1
            stack[top] = c
    
        elif c == ')':
            if top >= 0 and stack[top] == '(':
                top -= 1
            else:
                return 0
            
        elif c == '}':
            if top >=0 and stack[top] == '{':
                top -= 1
            else:
                return 0
    
    if top >= 0:
        return 0
    
    return 1

def op(line):
    stack = [0]*100
    top = -1
    
    for c in line:
        if c not in [')', '}']:
            top += 1
            stack[top] = c
        
        elif c == ')' : 
            res = 0
            while top >= -1 and stack[top] != '(':
                res += int(stack[top])
                top -= 1
            
            top -= 1
            top += 1
            stack[top] = res
    
        elif c == '}':
            res = 1
            while top >= 1 and stack[top] != '{':
                res *= int(stack[top])
                top -= 1
            top -= 1
            top += 1
            stack[top] = res
            
    if top != 0: # top이 남아있다 == 숫자가 남아있다.
        return -1
    
    else: 
        return stack[top]

T = int(input())
for tc in range(1, T+1):
    answer = -1
    line = input()
    
    if check(line) == 1:
        answer = op(line)

    print(f'{tc} {answer}')
