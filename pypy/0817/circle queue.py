size = 10
cq = [0]*size
front = rear = 0

def enqueue(item):
    global rear
    if isFull():
        print('full')
        return
    rear = (rear+1)%size
    cq[rear] = item

def dequeue():
    global front
    if isEmpty():
        print('empty')
        return
    front = (front+1)%size
    return cq[front]

def isEmpty():
    return rear == front

def isFull():
    return (rear+1)%size == front



#
# def enqueue(item):
#     global rear
#     # 큐가 가득차있으면 삽입X
#     if isFull():
#         print('full')
#         return
#     rear = (rear+1) % size
#     cq[rear] = item
#
# def dequeue():
#     global front
#     if isEmpty():
#         print('empty')
#         return
#     front = (front+1) % size
#     return cq[front]
#
# def isFull():
#     return front == rear # T/F형식으로 나옴
#
# def isEmpty():
#     return (rear+1) % size == front
#
# for i in range(size):
#     enqueue(i)
# for i in range(10):
#     enqueue(i)
#
# print(cq)
# print(isEmpty())
# print(isFull())
#
# for i in range(10):
#     print(dequeue(), end="")
#     print()
#
# print(cq)
# print(isEmpty())
# print(isFull())
#
