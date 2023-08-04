arr = [3, 6 ,7, 1, 5, 4]

n = len(arr) # n : 집합의 원소의 개수
# arr의 부분집합의 개수 2^6 == 1<<6 == 1*2^6
# 3<< 4 == 3*2^4

# 모든 부분집합을 검사
for i in range(1<<n): # 부분집합의 개수만큼 반복
    # i번째 부분집합을 검사하겠다.
    # i번째 부분집합이 n개의 원소중에 j번째 원소를 포함하는지
    sum = 0
    for j in range(n): # 원소의 개수가 n => n 번 검사
        if i & (1 << j):
            sum += arr[j]
            # 부분집합 i가 j번째 원소를 포함했는지 검사
            print(arr[j], end = ",") # j번 원소 출력

    if sum == 0:
        anwer = 1

    print()
print()