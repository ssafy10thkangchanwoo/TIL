# Queue 초기화
size = 10
q = [0]*size
front = rear = -1

# 삽입연산
def enqueue(item):
    global rear
    if isFull():
        print("full")
        return
    rear += 1
    q[rear] = item

# 삭제 연산
def dequeue():
    global front
    if isEmpty():
        print("empty")
        return
    front += 1
    return q[front]
    # 삭제하기 전에 큐가 비어있는지 확인

# 큐가 가득 찼는지?
def isFull():
    return rear == size -1

# 큐가 비어있는지?
def isEmpty():
    return front == rear

for i in range(10):
    enqueue(i)

print(q)
print(isEmpty())
print(isFull())

for i in range(10):
    print(dequeue(), end="")
    print()

print(q)
print(isEmpty())
print(isFull())

