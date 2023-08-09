T = int(input())

for tc in range(1, T+1):
    text = input()
    size = 1000
    stack = [0]*size
    top = 0
    stack[top] = text[0]


    for c in range(1, len(text)):
        if top >= 0 and stack[top] == text[c]:
            top -=1
        else:
            top += 1
            stack[top] = text[c]


    print(f'#{tc} {top+1}')


