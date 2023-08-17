T = 10
for tc in range(1, T+1):
    # 후위표기식만들기
    def get_postfix(infix, n):
        postfix = '' # 후위표기입력란생성
        stack = []

        # 후위표기 글자 떼오기
        for i in range(n):
            if infix[i] not in '+*': # 숫자면 후위표기식란에 넣기
                postfix += infix[i]

            else:
                # 스택이 비었으면 연산자를 스택에 넣음
                if not stack:
                    stack.append(infix[i])
                else:
                    if stack[-1] == "*":
                        postfix += stack.pop()
                    stack.append(infix[i])
        # 나머지 연산자 처리
        while stack:
            postfix += stack.pop()

        return postfix
    #후위표기식 계산 함수
    def get_result(postfix):
        stack = []
        for c in postfix:
            # 숫자면 스택에 정수화하여 넣는다.
            if c not in "+*":
                stack.append(int(c))
                #숫자가 아니면 스택에서 두개 뽑고 계산한다.
            else:
                n1 = stack.pop()
                n2 = stack.pop()

                if c == '+':
                    result = n1 + n2
                if c == '*':
                    result = n1 * n2
                # 계산 결과를 다시 스택에 넣는다.
                # 다시 result를 피연산자로 활용
                stack.append(result)
        # 마지막 stack(결과값)만 남았음
        return stack.pop()

    n = int(input())

    string = input()

    postfix = get_postfix(string, n)

    print(f'#{tc} {get_result(postfix)}')

