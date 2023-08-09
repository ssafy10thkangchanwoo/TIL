# T = int(input())
# for tc in range(1, T+1):
#     text = list(input())
#     long = len(text)
#
#     for i in range(long-1):
#         if text[i] == text[i+1]:
#             text[i]

T = int(input())
for tc in range(1, T+1):
    text = input()
    size = 1000
    stack = [0] * size
    top = -1 # 마지막으로 삽입한 원소의 위치

    # 스택을 이용해서 풀껀데
    # 일단 문자를 스택에 넣어(맨 처음 글자는 넣음)
    top += 1
    stack[top] = text[0]
    # 두번째 글자부터는 내가 제일 최근에 넣었던 글자와 비교해서
    for i in range(1, len(text)):
        if top != -1 and stack[top] == text[i]:
            top -= 1
    else:
        top += 1
        stack[top] = text[i]

    # 마지막으로 원소가 삽입한 위치 + 1 == 스택의 크기
    print(f"#{tc} ")

    # 만약 같다면 스택에서 pop
    # 다르다면 현재 글자를 스택에 push
