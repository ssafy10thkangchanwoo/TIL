
def backtrackig(cnt):
    # 기저 조건
    # 숫자 3개를 골랐을 때 종료
    if cnt == 3:
        print(*path)
        return 
    
    for num in arr:
        if num in path:
            continue
    # 들어가기 전 
        path[cnt] = num 
        # 다음 재귀 함수 호출
        backtrackig(cnt+1)
        # 돌아와서 할 로직
        path[cnt] = 0

arr= [i for i in range(1, 4)]
path =[0] * 3

backtrackig(0)


# def func():
    # 재귀를 끝내는 기저조건
    # 가지치기

    # 반복문
        # 가지치기
        # 재귀 들어가기 전 
        # 재귀함시 호출
        # 돌아와서 초기화