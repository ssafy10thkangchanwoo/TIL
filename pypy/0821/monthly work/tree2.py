class Node:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")

root = A
A.left = D
E.left = B
E.right = C

def preorder(Node):
    if Node:
        print(Node.data)
        preorder(None.left)
        preorder(None.right)

preorder(A)
