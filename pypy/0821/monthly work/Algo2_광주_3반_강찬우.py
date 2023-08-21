# 테스트 케이스 개수
T = int(input())
# tc번째 테스트
for tc in range(1, T+1):
    # N : 카드 개수, M : 김싸피의 순서
    N, M = map(int,input().split())
    # 기존 덱
    arr = list(input().split())
    print(arr)
    # 짝수 숫자를 넣을 덱 B와 홀수 숫자를 넣을 덱 C
    B = []
    C = []
    # 보너스 카운트
    bonus = 0
    # 각 추출 시 뽑은 카드 숫자 + 보너스를 덱에 넣을 요소 값으로 설정
    # 기존덱에서 B,C덱의 요소 추출
    for i in range(N): # arr[i] = 각 요소랑 비교 좀 해라.. 3번째 넘은 듯
            if arr[i] == '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9' or '10' or '11' or '12' or '13':
                n = int(arr[i]) + bonus
            else:
                bonus += 1
            if n % 2:
                B.append(n)
            else:
                C.append(n)
     
    #     if arr[i] == '+':
    #         bonus += 1
    #     elif arr[i] == '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9' or '10' or '11' or '12' or '13': # 이것보단 else가 낫다.
        
    #         n = int(arr[i]) + bonus
    #         if n % 2:
    #             B.append(n)
    #         else:
    #             C.append(n)
    # B, C 덱에서 B는 왼쪽에서 C는 우측에서 하나씩 뽑아서 김싸피의 순서 전까지 제거
    for _ in range(M-1):
        # B에 원소가 있을 때만 제거하도록 함.
        if B:
            B.pop(0)
        if C:
            C.pop()
    # 이제 싸피차례로 B, C 덱에 원소가 있는 경우 싸피는 해당 점수를 획득한다.
    # B, C 덱에 원소가 없을 경우에는 0점을 획득한다.
    if B:
        ssafy_B = B.pop(0)
    else:
        ssafy_B = 0
    if C:
        ssafy_C = C.pop()
    else:
        ssafy_c = 0
    # B, C덱에서 추출한 점수를 합산
    answer = ssafy_B + ssafy_C
    # 결과 출력
    print(f'#{tc} {answer}')
