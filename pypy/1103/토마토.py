def search():
    global day
    while True:
        Nozero = 0
        for i in range(1, H+1):
            for j in range(1, W+1):

                if Nozero == H*W:
                    break  
                if matrix[i][j] == 0:
                    for d in range(4):
                        if matrix[i+dr[d]][j+dc[d]] == 1:
                            turnbox.append((i,j))
                else:
                    Nozero += 1

        if turnbox:
            for (i,j) in turnbox:
                matrix[i][j] = 1
                day += 1



dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


W, H = map(int,input().split())


matrix = [[-1]+list(map(int,input().split()))+[-1] for _ in range(H)]
matrix = [[-1]*(W+2)] + matrix + [[-1]*(W+2)]
day = 0
sp = []
possible = True 
for i in range(1, H+1):
    for j in range(1, W+1):
        if matrix[i][j] == 1:
            sp.append((i,j))
            count = 0 
            for d in range(4):
                if matrix[i+dr[d]][j+dc[d]]== -1:
                    count += 1
                if count == 4:
                    possible = False 

turnbox = []
if possible:
    search()
else:
    day= -1

print(day)
# for i in range(1, H+1):
#     for j in range(1, W+1):
#         if matrix[i][j] == 0:
#             for d in range(4):
#                 if matrix[i+dr[d]][j+dc[d]] == 1:
#                     turnbox.append((i,j))

# if turnbox:
#     for (i,j) in turnbox:
#         matrix[i][j] = 1
#         day += 1

