v1 = 100
v2 = v1

print(v1, v2)

v1 = 50

print(v1,v2)

v3 = [1,2,3] * 2
v4 = v3

# 리스트 안의 요소는 가변하다.
print(v3, v4)

v4[0] = -1

print(v3,v4)

a = [[500,100,300]]*3
a[0][0] = -1
print(a)
