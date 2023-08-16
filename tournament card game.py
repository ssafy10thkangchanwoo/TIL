#
# def tournament(i,j):
#
#     # 종료조건
#     # 더 이상 쪼갤 수 없을 때 -> i~j까지 사이에 있는 사람이 1명
#     if i == j:
#         # i번째 사람이라고 return
#         return i
#     # 재귀호출
#     else:
#         # 왼쪽부분
#         left = tournament(i, (i+j)//2)
#         # 오른쪽 부분
#         right = tournament((i+j)//2+1, j)
#
#         #왼쪽과 오른쪽 중에서 승자를 골라서 return
#         # card[left] -> 왼쪽 사람이 낸 패
#         # card[right] -> 오른쪽 사람이 낸 패
#
#         # 승자를 판별하는 코드
#     return winner(left, right)
#
# def winner(Start, End):
#     if End-Start == 1:
#         if card[Start] == 1 and (card[End] == 3 or card[End]==1):
#             return Start
#         elif card[Start] == 2 and (card[End] ==1 or card[End]==2):
#             return Start
#         elif card[Start] == 3 and (card[End] ==2 or card[End] == 1):
#             return Start
#
# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#
#     card = list(map(int,input().split()))
#     i = 0
#     j = N-1
#     winner = tournament(i,j)
#     print(f'#{tc} {i}')




T = int(input())
for tc in range(1, T+1):
    Start = 1
    End = int(input())
    card = list(map(int,input().split()))

    def winner(Start, End):
        if End-Start == 1:
            if card[Start] == 1 and (card[End] == 3 or card[End]==1):
                return Start
            elif card[Start] == 2 and (card[End] ==1 or card[End]==2):
                return Start
            elif card[Start] == 3 and (card[End] ==2 or card[End] == 1):
                return Start

        else:
            winner(Start, (Start+End)//2), winner((Start+End)//2+1, End)

    victory = winner(Start,End)
    print(f'#{tc} {victory}')


