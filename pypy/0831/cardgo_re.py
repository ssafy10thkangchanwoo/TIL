T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 작업의 수

    # [(s1,e1), (s2,e2)..]
    # s1:1번 작업시작시간, e1: 1번 작업 종료 시간
    work_list = list(map(int,input().split()))

    # work_list를 작업 종료 시간이 빠른게 앞에 오도록 정렬
    work_list.sort(key=lambda item: item[1])
     
    # 같은 의미
# def key_f(item):
#     return item[1]

#     work_list.sort(key=key_f)

    # 최대 작업 개수
    count = 0

    # 이전 작업이 끝난 시간
    time = 0

    while work_list:
        # 다음 작업을 꺼내온다.
        next_work = work_list.pop(0)
        
        # 다음 작업시작시간이 이전 작업이 끝난 시간보다 크거나 같으면
        if next_work[0] >= time:
            count += 1
            # 작업 했으니까 이전 작업 끝난 시간 최신화
            time = next_work[1]

    print(f'{tc} {count}')