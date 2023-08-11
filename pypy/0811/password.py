T = 10
for tc in range(1, T+1):
    str_long, str_numbers = input().split()
    long = int(str_long)
    stack = [0] * long # [] * n 과 [0] * n의 차이에 대해
    top = -1

    for t in str_numbers:
        if top >= 0 and stack[top] == t:
            top -= 1
        else:
            top += 1
            stack[top] = t

    print(f'#{tc} {stack}')



















# T = 10
# for tc in range(1,11):
#     str_N, str_num = input().split()
#
#     N = int(str_N)
#     stack = [0]*N
#     top = -1
#
#     for t in str_num:
#         if top==-1 or stack[top] != t: # 스택이 비어있거나, top 원소와 다르면
#             top += 1# push(t)
#             stack[top] = t
#         else:  # stack이 차있거나 top과 같으면
#             top -= 1
#     ans = ''.join(stack[:top+1])
#
#     print(f'#{tc} {ans}')