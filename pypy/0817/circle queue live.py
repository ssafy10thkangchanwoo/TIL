def enq(data):
    global rear
    global front
    if (front+1)%cQsize == front:
        front = (front+1)%cQsize
    rear = (rear+1) % cQsize
    return cQ[front]


cQsize = 4
cQ = [0] * cQsize
front = 0
rear = 0