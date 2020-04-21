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
        temp = self.head
        if self.head == None:
            self.head = newNode
        elif info < temp.info:
            if temp.left == None:
                print(self.head.info)
                self.head.left == newNode
            else:
                temp = temp.left()

t = Tree()
t.addNode(6)
t.addNode(3)
t.addNode(1)
n = ()
print(t.head.left)