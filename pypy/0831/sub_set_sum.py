def subset(i, N): # i개로 부분집합 만들기
    if i==N: # i가 N개가 되면 
        s = 0 #
        for j in range(N): #
            if bit[j]: 
                s += arr[j]
        # if s == 0:
        #     for j in range(N):
        #         if bit[j]:
        #             print(arr[j], end='')
        #             print()
    else:
        bit[i] = 1 # i번째 비트에 와서 i=1로 했습니다. 
                    # 그런데 이러면 항상 i는 
        subset(i+1, N)

arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2] # 집합
N = len(arr) # 집합의 길이
bit = [0]*N # 이건 어디에 쓸까?
subset(0, N) 