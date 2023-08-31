def swap(cnt):
    # 종료 조건 : 교환조건을 다 소모했다면
    # 바꾼 결과물을 숫자로 바꿔서 최대 상금 계산
    if cnt == N:

        return
    
    # 자리를 바꿀 위치 2개를 교환 한번 할때마다 새로 지정해줘야한다.
    # 이 문제에서는 동일한 위치에서 중복 교환을 허용하기 때문이다.
    # 바꿀 위치중에 앞쪽 : i
    # 바꿀 위치중에 뒤쪽 : j 
    for i in range(len(S)-1):
        for j in range(i+1, len(S)):
            S[i], S[j] = S[j], S[i]
            swap(cnt+1)
            # 바뀐위치 원상복구
            S[i], S[j] = S[j], S[i]

T = int(input())
for tc in range(1,T+1):
    S, N = input().split()

    S = list(S)
    N = int(N)
    print(swap(0))