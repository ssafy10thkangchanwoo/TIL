def funfun(n):

    #  재귀함수 만들 때 꼭 필요한 조건
    # 1. 종료 조건
    if n == 0 :
        print(f'{n} : 끝')
        return
    


    # 2. 재귀 호출
    else:
        print(n)
        funfun(n-1)
        # 여기서 ff -9~ 0까지 .
        # 근데 아래에 109876 이어지고 있음


        print(n)

funfun(10)