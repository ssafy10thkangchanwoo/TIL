pat = {
    "001101" : 0,
    "010011" : 1,
    "111011" : 2,
    "110001" : 3,
    "100011" : 4,
    "110111" : 5,
    "001011" : 6,
    "111101" : 7,
    "011001" : 8,
    "101111" : 9,
}

hex1='0DEC'
hex2='0269FAC9A0'

def find_pattern(hex_string):
    # hex_string은 16진수 문자열
    # 이진수 문자열로 바꾸면 길이가 4배
    l = len(hex_string)*4
    x = int(hex_string, 16) # 10진수로 변환
    # 숫자를 다시 이진수 문자열로 바꾸기
    bin_string = ''

    # i번째 비트를 검사해서 결과가 0 -> i번째 비트는 0
    # 결과가 0이 아니면(1이면) i번째 비트는 1
    for i in range(l-1,-1,-1):
        bin_string += '1' if x & (1<<i) else '0'
    
    # 가변타입 리스트 변환
    bin_string = list(bin_string)

    # 뒤에서부터 검사를 해서 1을 만나면 암호 해독 시작
    # 1을 만난 순간부터 6개씩 잘라서 암호해독 시작
    password = ''
    for j in range(l-1, 5, -1): # 6개씩 자르니까 조정
        # 1 만난 순간 6개씩 만잘라 검사
        if bin_string[j] == '1':
            
            code=bin_string[j-5:j+1]
            
            # 코드가 있는지 검사
            dec = pat.get(code)

            if dec != None:
                result += str(dec)
                
                #암호코드 변경한 나머지 5칸에서는 패턴을 또 안찾도록
                for j in range(i, i-6, -1):
                    bin_string[j] = '0'

            dec = int(pw,2)
            
            password.append(dec)