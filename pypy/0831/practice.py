list = [1,2,3,4,5]
N = 5
R = 3


# 내가 idx 번째 숫자를 고를지 안고를지
# r번 골랐다면 종료 또는 n번 고를지 안고를지 선택을 다 완료했다면

def comb(idx, r, selected):
    # idx가 5번을 볼 차례일 때, r의 갯수가 R개라면
    if idx == N:
        if r == R:
            # R 개 골랐을 때만
            print([list[i] for i in selected])  # selected에 있는 원소 하나씩 빼온다.
        return
    # 내가 idx번째에 있는 숫자를 골랐다.
    selected.append(idx) # selected에 idx위치를 추가한다.
    comb(idx + 1, r + 1, selected) # idx위치를 1칸 올리고 selected에 새로운 원소가 저장되었고 그 개수는 1개 증가했다.
    # 내가 idx번째에 있는 숫자는 안골랐다..
    selected.pop() # 다른쪽 재귀함수..selected원소를 삭제했다.
    comb(idx+1, r, selected) # 변경되지 않는 selected와 개수 r, 하지만 탐방할 인덱스번호는 증가했다.

comb(0,0,[])  # 시작 idx위치, 갯수, 원소들