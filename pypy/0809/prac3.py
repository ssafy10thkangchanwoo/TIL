T = int(input())

for tc in range(1, T+1):
    row = input()
    
    stack = []
    answer = 1
    # 아래는 answer = 0 으로 만들 조건들 열거
    for c in row:
        if c == "(":
            stack.append(c)
        
        if c == ")":
            if len(stack) == 0 : 
                answer = 0
                break
                #나오고 아무 것도 없다 -> 괄호개수가 다르다. )이 더 많다
            
            # 같은 괄호에서 왼쪽 괄호는 오른쪽 괄호보다 먼저 나와야 한다.??
            # 괄호 사이에는 포함관계만 존재한다.
            b= stack.pop()
            if not(b == '('):
                answer = 0
                break

    # 글자 검사 끝난 후 스택에 남아있는 것이 있나?
    # 3. 왼쪽 괄호와 오른쪽 괄호 개수가 같아야 한다.
    # ( 이 더 많다
    if len(stack) > 0 :
        answer = 0
       

    print(f'#{tc} {answer}')
