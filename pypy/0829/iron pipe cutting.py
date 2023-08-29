T = int(input())
for tc in range(1, T+1):
    pipe = input()
    stack = []
    lager = []
    for i in range(len(pipe)):
        if pipe[i] == '(':
            stack.append(pipe[i])
        else:
            if stack:
                if stack[-1] == '(':
                    stack.pop()
                    lager.append(i)

