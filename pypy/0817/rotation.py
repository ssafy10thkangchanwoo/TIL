T = int(input())
def dequeue():
    global front
    front = front+1
    return new[front]

def enqueue(item):
    global rear
    rear = rear+1
    new[rear] = item
    return

for tc in range(1, T+1):
    N, M = map(int,input().split())
    matrix = [0]*1000
    idx = list(map(int, input().split()))
    new = idx + matrix
    rear = N-1
    front = -1

    for _ in range(1, M+1):

        enqueue(dequeue())

    answer = new[front+1]

    print(f'#{tc} {answer}')



