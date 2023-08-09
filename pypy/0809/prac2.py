top = -1
size = 10
stack = [0]*size

def my_push(i):
    global top
    top += 1
    if top <= size:
        stack[top] = i
    else:
        return

for i in range(10):
    my_push(i)



def my_pop():
    global top
    if top == -1:
        print('underflow')
        return 
    else: 
        top -= 1
        return stack[top + 1]



def peek():
    if top > -1:
        return stack[top]

print(stack) # stack 원소는 그대로

print(top)