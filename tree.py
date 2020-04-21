class node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.head = None
    
    def addNode(self, info):
        newNode = node(info)
        if self.head == None:
            self.head = newNode
        elif info < self.head.info:
            self.head.left = newNode

t = Tree()
t.addNode(6)
t.addNode(3)
print(t.head.left.info)