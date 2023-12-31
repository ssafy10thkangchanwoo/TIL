

# 연결리스트로 저장
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None 
        self.right = None
    
    # 삽입함수
    def insert(self, childNode):
        # 왼쪽 자식이 없을 경우
        if not self.left:
            self.left = childNode
            return 
        
        # 오른쪽 자식이 없을 경우
        if not self.right:
            self.right = childNode
            return
        
        return
        
    # 순회
    # 전위
    def preorder(self):
        # 아무것도 없는 트리를 조회할 때
        if self != None:
            print(self.value, end='')
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()
            

arr = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6]
# 이진 트리 만들기
nodes = [TreeNode(i) for i in range(1, 14)]
for i in range(0, len(arr), 2):
    parentNode = arr[i]
    childNode = arr[i+1]
    nodes[parentNode].insert(nodes[childNode])

nodes[i].preorder()