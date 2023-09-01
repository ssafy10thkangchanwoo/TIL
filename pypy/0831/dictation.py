list = [1, 2, 3, 4, 5]
N = 5
R = 3

count = 0


def comb(idx, r, selected):
    global count
    if idx == N:
        # k = sum(selected)
        subset = [list[i] for i in selected] # subset은 이쪽 selected에 들어있는 원소들의 리스트이다.
        if sum(subset) == 0: # 섭셋값들이 0이면
            count += 1 #카운트를 증가시킨다.
            print(subset)
        # if r == R: # 이러면 3개짜리만 보는거
        
        return
    selected.append(idx)
    comb(idx+1, r+1, selected)
    selected.pop()
    comb(idx+1,r,selected)
list = [-1,3,-9,6,7,-6,1,5,4,-2]
N = len(list)
comb(0,0,[])

