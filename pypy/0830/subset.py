a = [3,6,7,1,5,4]
subset1 =[]
N = 6
# for i in range(1, (1<<N)-1): 
for i in range(1, (1<<N)//2):
    subset1=[]
    subset2=[]
    for j in range(N):
        if i&(1<<j): #j번 비트가 0이 아니면
            subset1.append(a[j])
        else:
            subset2.append(a[j])
    print(subset1, subset2)