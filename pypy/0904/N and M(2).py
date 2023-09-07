N, M = map(int,input().split())
sub_list = []
for i in range(1, M+1): #1부터 M.. 이러면 두개 고정임;
    for j in range(1, N+1):
       if i != j:
        sub_list.append((i, j))
for i in range(len(sub_list)):
   print(*sub_list[i])