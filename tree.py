class node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.head = None
    
    def ii(self):
        print('function')

    def printTree(self):
        temp = self
        if temp.head.left:
            temp.head = temp.head.left
            temp.printTree()
        print(temp.head.info)
        if temp.head.right:
            temp = temp.head.right
            self.printTree()
    
    def addNode(self, info):
        if self.head == None:
            self.head = node(info)
            return
        temp = self.head
        while temp:
            if info < temp.info:
                if temp.left == None:
                    temp.left = node(info)
                    return
                else:
                    temp = temp.left
            else:
                if temp.right == None:
                    temp.right = node(info)
                    return
                else:
                    temp = temp.right
            

t = Tree()
t.addNode(6)
t.addNode(3)
t.addNode(1)
t.printTree()
n = ()