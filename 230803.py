
n, m = 3, 4

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

# for j in range(n):
#     for i in range(m):
#         print(matrix[i][j])

for i in range(n):
    for j in range(m):
        print(matrix[i][j+ (m-1-2j)*(i%2)])
    

        