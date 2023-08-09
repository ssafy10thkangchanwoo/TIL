# 스택사용 (파이썬 메소드)

# stack = []
# def py_push(item):
#     stack.append(item)

# def py_pop():
#     if len(stack) == 0:
#         # underflow
#         return 
#     else:
#         return stack.pop()
    


# for i in range(10):
#     py_push(i)

# print(stack)

# for i in range(10):
#     print(py_pop(), end= " ")

# print()
# print(stack)



# 스택 사용(인덱스)
top = -1 # 원소를 마지막으로 삽입할 위ㅣ
size = 10
stack = [0] * size

def my_push(item):
    global top
    top += 1
    if top == size:
        print('overflowe')
    else:
        stack[top] = item

def my_pop():
    global top
    if top == -1:
        print('underflow')
        return 
    else: 
        top -= 1
        return stack[top + 1]
    
def peek():
    # top이 -1이면 원소가 없다.
    if top > -1:
        return stack[top]
    
for i in range(10):
    my_push(i)

print(stack)

for i in range(10):
    print(my_pop(), end= ' ')

print()
print(stack)
