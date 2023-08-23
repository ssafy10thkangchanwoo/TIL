# def calculate(s):
#     global cleft
#     global cright
#     global calculating_box
#
#     if s <= N:
#         if cleft[s] != 0:
#             left_val = calculate(cleft[s])
#         else:
#             left_val = int(calculating_box[s])
#
#         if cright[s] != 0:
#             right_val = calculate(cright[s])
#         else:
#             right_val = int(calculating_box[s])
#
#         if calculating_box[s] == '+':
#             return left_val + right_val
#         elif calculating_box[s] == '-':
#             return left_val - right_val
#         elif calculating_box[s] == '*':
#             return left_val * right_val
#         elif calculating_box[s] == '/':
#             return left_val / right_val
#         else:
#             return int(calculating_box[s])
#     else:
#         return int(calculating_box[s])  # 여기서 leaf 노드의 값을 반환합니다.


def calculate(s):
    global cleft
    global cright
    global calculating_box

    if s <= N and cleft[s] != 0 and cright[s] !=0:
        calculate(cleft[s])
        calculate(cright[s])
        if calculating_box[s] in '+':
            return int(calculating_box[cleft[s]]) + int(calculating_box[cright[s]])
        elif calculating_box[s] in '-':
            return int(calculating_box[cleft[s]]) - int(calculating_box[cright[s]])
        elif calculating_box[s] in '*':
            return int(calculating_box[cleft[s]]) * int(calculating_box[cright[s]])
        elif calculating_box[s] in '/':
            return int(calculating_box[cleft[s]]) / int(calculating_box[cright[s]])
        else:
            return int(calculating_box[s])
    else:
        return


T = 10
for tc in range(1, T + 1):
    N = int(input())
    calculating_box = [0] * (N + 1)
    cleft = [0] * (N + 1)
    cright = [0] * (N + 1)
    for i in range(1, N + 1):
        text = list(input().split())
        long = len(text)
        if long == 4:
            cleft[i] = int(text[2])
            cright[i] = int(text[3])
        elif long == 3:
            cleft[i] = int(text[2])
        calculating_box[i] = text[1]

    answer = int(calculate(1))
    print(f'#{tc} {answer}')
