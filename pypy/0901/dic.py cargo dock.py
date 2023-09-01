T = int(input())

for tc in range(1, T+1):
    N = int(input())

    work_list = [list(map(int, input().split())) for _ in range(N)]

    work_list.sort(key=lambda item:item[1])

    count = 0
    time = 0

    while work_list:
        next_work = work_list.pop(0)

        if next_work[0] >= time:
            count += 1
            time = next_work[1]