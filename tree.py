class node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.head = None

    def printTree(self):
        if self.head.left == None and self.head.right == None:
            print ("-" + self.info)
        else:
            print('*')
            if self.head:
                print(self.head.left.info)
                self.head.left.printTree()
            elif self.head.right:
                print('$')
                self.right.printTree()
    
    def addNode(self, info):
        newNode = node(info)
        temp = self.head
        if self.head == None:
            self.head = newNode
        elif info < temp.info:
            if temp.left == None:
                self.head.left == newNode
            else:
                temp = temp.left()

t = Tree()
t.addNode(6)
t.printTree()
n = ()