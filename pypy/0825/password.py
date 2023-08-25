table = {
    (2, 1, 1) : 0,
    (2, 1, 1) : 1,
    (1, 2, 2) : 2,
    (4, 1, 1) : 3,
    (1, 3, 2) : 4,
    (2, 3, 1) : 5,
    (1, 1, 4) : 6,
    (3, 1, 2) : 7,
    (2, 1, 3) : 8,
    (1, 1, 2) : 9,
}
T = int(input())

for tc in range(1, T+1):
    N, M = map(int,input().split())

    # 출력할 결과
    result = 0

    # 코드 중복 체크 방지
    dup_check = []

    # 암호코드 # set으로 각 줄에 대한 중복 처리
    arr = list(set([input()[:M] for _ in range(N)]))

    # 각 줄에 대해 코드 검사
    for i in range(len(arr)):
        #i번째 줄에서 검사
        ith_row = arr[i]
        # i번째 줄 16진수 문자열을 2진수 문자열로 바꾸기
        bin_row =''


        # i번째 줄 문자열에서 문자 하나씩 떼서 2진수 문자열로
        for c in ith_row:

            c_hex_to_dec = int(c, 16)
            # 16진수 하나는 2진수 * 4 
            for j in range(3, -1, -1):
                bin_row += '1' if c_hex_to_dec & (1 << j) else '0'

        # i번째 문자열을 2진수로 바꿨는데 안에 1이 없다 
        if '1' not in bin_row:
            # 다음줄 검사
            continue
        else: 
            # i번째 줄 안에 1이 있다- > 뒤에서부터 암호코드 만들기 시작
            # 0과 1의 비율, 0 1 0 1 순서로 나온다.
            ratio = [0]*4
            # radio[0] : 맨 처음 0 비율
            
            # 모든 암호 코드는 마지막이 1로 끝나니까 오른쪽 0은 모두 제거
            bin_row = bin_row.rstrip('0')

            # 현재 i번째에서 만든 코드
            code = []
            # 코드의 맨 끝이 1이니까 뒤에서부터 비율을 계산
            for j in range(len(bin_row)-1, -1, -1):
                if bin_row[j] == '1' and ratio[2] == 0:
                    # 마지막 1 비율 계산중..
                    ratio[3] += 1
                elif bin_row[j] == '0' and ratio[1] == 0:
                    # 세번째 0 비율 계산중..
                    ratio[2] += 1
                elif bin_row[j] == '1' and ratio[0]:
                    # 두번째 1의 비율 계산
                    ratio[1] += 1
                elif bin_row[j] == '0' and bin_row[j-1] == '1':
                    # 처음 부분 0을 만났다. 이 부분은 계산 안해도 코드판별 가능
                    # 여기서 코드 변환 작업 시작
                
                
                min_v = min(ratio[1:4])
                # 비율 계산 후 이 비율로 된 숫자가 테이블 안에 있는지 확인
                number = table.get(ratio[1] // min_v, ratio[2] // min_v, ratio[3] // min_v)
                
                # 숫자 하나 만든거 코드에 이어붙이기
                code.append(number)

                # 비율계산 다 하고 초기화
                ratio = [0]*4

                # 만들고 나서 코드의 길이가 8이다 ==> 암호코드 판별
                if len(code) == 8:
                    code = code[::-1]
                    # 검증코드 계산
                    odd = code[0] + code[2] + code[3] + code[6]
                    even = code[1] + code[3] + code[5] + code[7]
                    # 계산결과를 10으로 나누어서 떨어지면 올바른 코드
                    if (odd * 3 + even)% 10 == 0 and code not in dup_check:
                        # 각 자리수를 더해서 답에 누적합
                        result += odd + even
                        # 중복처리
                        dup_check.append(code)

                    code = []

    print(f'#{tc} {result}')

                    