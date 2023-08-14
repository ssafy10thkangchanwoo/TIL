T = int(input())

for tc in range(1, T+1):
    line = input()
    # 식의 계산 결과
    answer = -1
    # 1. 괄호 검사
    def check(line):
        stack = [0] * 100
        top = -1
        # 한글자씩 분리해서 괄호 검사
        for c in line:
            # 떼온 글자가 여는 괄호이면 push
            if c in ["(", "{"]:
                top += 1
                stack[top] = c

            # 떼온 글자가 닫는 괄호이면
            elif c == ')':
                # 스택이 비어있는지 확인
                if top >= 0 and stack[top] == '(':
                    top -= 1
                else:
                    return 0

            elif c == '}':
            # 스택이 비어있는지 확인
            if top >= 0 and stack[top] == '}':
                top -= 1
            else:
                return 0
            # 스택 안에서 꺼내와서 짝 비교


    # 2. 식 계산
def op(line): # 괄호가 정상인 수식을 계산하여 결과를 얻는 함수
    stack = [0] * 100
    top = -1

    # 한글자씩 분리
    for c in line:
        # 닫는 괄호가 나올때까지 stack에 push
        # 닫는 괄호가 나오면 그 때 계산을 시작할 것
        if c not in [')', '}']:
            top += 1
            stack[top] = c
        # 닫는 괄호가 나오면 계산 시작
        elif c == ')' : # "(" 가 나올 때까지 스택에서 꺼내서 더하기
            res = 0 # 이 괄호에서의 계산 결과
            # 스택에 더할 숫자가 남아 잇고, 맨 위 원소가 "("가 아니면 더하기
            while top > -1 and stack[top] != '(':
                res += int(stack[top])
                top -= 1 #pop
            # while문이 끝났으면 아직 여는 괄호가 스택에 하나 남아 있으니까 제거
            top -= 1 # "(" pop

            # 계산 결과를 나중에 다른 괄호에서 쓰기 위해 stack push
            top += 1
            stack[top] = res

        elif c == '}':
            res = 1  # 이 괄호에서의 계산 결과
            # 스택에 더할 숫자가 남아 잇고, 맨 위 원소가 "{"가 아니면 더하기
            while top > -1 and stack[top] != '{':
                res *= int(stack[top])
                top -= 1  # pop
            # while문이 끝났으면 아직 여는 괄호가 스택에 하나 남아 있으니까 제거
            top -= 1  # "{" pop

            # 계산 결과를 나중에 다른 괄호에서 쓰기 위해 stack push
            top += 1
            stack[top] = res

    # 반복이 다 끝나고 나면 스택에 최종 계산 결과가 남아있다.
    return stack[top]







    if check(line) == 1:
    print(f'#{tc} {answer}')