T = int(input())

for tc in range(1, T+1):
    # 2차원 배열의 크기 N, 회문의 길이 M
    N, M = map(int, input().split())

    # 글자 모음 (2차원 배열로 만들기)
    text = [list(input()) for _ in range(N)]

    # 우리 찾는 회문
    answer = ""



    # 행 우선 순회
    for i in range(N): # i는 행번호
        for j in range(N-M+1): # j는 열번호
            # (i,j)위치에 있는 글자부터 회문을 만들기 시작
            # 회문의 길이가 m이니까 (i,j) ~ (i, j+m) 글자를 모아서
            # 문자열로 만들면 완성 -> 이 문자열이 회문인지 아닌지 검사
            # j범위 주의(인덱스 범위 벗어나지 않도록)

            # (i,j) 위치에서 문자열 만들기 시작
            word_row = ""
            # 글자 M개 모아서 문자열 만들기
            for k in range(M):
                word_row += text[i][j+k]
                # word_row가 회문인지 아닌지 판별 (인덱스연산)


            for m in range((M//2)):  # 나 숫자세기 못한듯?
                if word_row[m] != word_row[M-m-1]:
                    break
            else:
                answer = word_row




    # 열 우선 순회
    for j in range(N):
        for i in range(N-M+1):
            word_col = ''
            for k in range(M):
                word_col += text[i+k][j]
            count = 0
            for m in range((M//2)):  # 나 숫자세기 못한듯?
                if word_col[m] == word_col[M-m-1]:
                    count += 1
                if word_col[m] != word_col[M-m-1]:
                    break
                if count == (M//2)-1:
                    answer = word_col

    print(f'#{tc} {answer}')


# if와 elif의 차이
# x = 5
# if x > 3:
#     print("x is greater than 3")
# elif x < 10:
#     print("x is less than 10") # 이 줄은 실행되지 않음
#
# x = 5
# if x > 3:
#     print("x is greater than 3")
# if x < 10:
#     print("x is less than 10") # 이 줄은 실행됨


