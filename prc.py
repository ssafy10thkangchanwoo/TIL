T = 10
 
for tc in range(1, T+1):
    N = int(input())
    box = list(map(int, input().split()))
 
 
    def BubbleSort(a, N):
        for i in range(N-1, 0, -1):
            for j in range(0, i):
                if a[j] > a[j+1]:
                    a[j], a[j+1] = a[j+1],a[j]  
        return a
    
          
    for _ in range(N):
            sorted_box = BubbleSort(box, 100)
            sorted_box[0] += 1
            sorted_box[-1] -= 1
         
    sorted_box = BubbleSort(box, 100)
         
    print(f'#{tc} {sorted_box[-1] - sorted_box[0]}')

