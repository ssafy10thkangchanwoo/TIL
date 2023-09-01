# 오류발생
def swap(cnt):
    global answer
    val = ''.join(numbers)
    if (cnt, val) in visited: # cnt번 바꾸기 진행할건데 이전에 만든적이 있는 숫자면 진행X
        return
    # 전에 만든적 없는 숫자를 만들면 visited 체크 후 진행
    visited.add((cnt,val))

    if cnt==times: #이러면 그냥 다음 리스트에 가는거.
        # 해당 인덱스 위치에서 교환 후 후 손대지 않은 순열과 다르게 중복교환 가능하므로
        answer = max(answer, val)
        return
    
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            numbers[i], numbers[j] = numbers[j], numbers[i]
            swap(cnt+1)
            numbers[i], numbers[j] = numbers[j], numbers[i]



T = int(input())
for tc in range(1,T+1):
    numbers, times = list(map(int,input().split()))
    numbers = (list(str(numbers)))
    # 중복체크 할 set() 만들기
    visited = set() # (k, 내가 맞든 숫자): 자리를 k번 교환했을 때 지금 숫자를 만든 적이 있다.
    answer = 0
    cnt = 0
    swap(0)
    print(f'#{tc} {answer}')