T = int(input())

for tc in range(1, T+1):
    text = input()
    box = []
    answer = 1

    for c in text:
        if c == '(' or c ==')' or c =='{' or c =='}':
            box.append(c)

    stack = []
    for c in box:
        if c == '(' or c =='{':
            stack.append(c)

        if c == ')':
            if len(stack) == 0:
                answer = 0
                break

            b = stack.pop()

            if not(b) == '(':
                answer = 0
                break

        if c == '}':
            if len(stack) == 0:
                answer = 0
                break

            b = stack.pop()

            if not(b == '{'):
                answer = 0
                break

    if len(stack) > 0:
        answer = 0


    print(f'#{tc} {answer}')


