T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    max_count = 0
    for i in range(len(str1)):
        counts = 0
        
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                counts += 1
            
            if max_count < counts:
                max_count = counts
            
    print(f'#{tc} {max_count}')



                           