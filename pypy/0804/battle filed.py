T = int(input())
for tc in range(1, T+1):
    H, W = map(int,input().split())
    # 매트릭스에 원소 배치
    matrix = [list(input().split()) for _ in range(H)]

    # 조작키 input
    manu_count = int(input())
    manu_key = input().split()

    for