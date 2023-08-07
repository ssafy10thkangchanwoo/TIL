# 고지식한 패턴 매칭 알고리즘 사용해보기

T = int(input())

for tc in range(1, T+1):
    pattern = input() # 내가 찾고자 하는 패턴 문자열
    text = input() # 여기 안에서 찾고 싶다

    # 일치하는 부분이 있으면 1, 없으면 0을 출력
    pidx = 0
    tidx = 0

    answer = 0 # 답

    # 비교 시작
    while tidx < len(text) and pidx < len(pattern):
        # 비교할 문자의 위치가 문자열의 길이보다 길면 안됨.
        # 현재 위치에서부터 비교를 시작한다.
        # 현재 위치 pi에 있는 문자와 ti에 있는 문자가 같으면
        if pattern[pidx] == text[tidx]:
        # pi와 ti 1씩 증가해 가면서 계속 비교(끝 or 다른게 나올 때까지)
            pidx += 1
            tidx += 1
        # 다르면?? pi는 0으로 바꾸고 ti는 pi만큼 다시 앞으로 갔다가
        else:
        # 다음 위치에서 비교를 해야하니까 1 증가
            tidx = tidx - pidx + 1
            pidx = 0


        #패턴 문자의 위치 pi가 패턴의 길이만큼 되버렸다면
        # 그전에 있던 모든 문자가 같았다는 의미다.
        # 패턴을 발견했다는 것을 의미한다.
        if pidx==len(pattern):
            answer = 1
            break

    print(f"#{tc} {answer}")

