class Tree:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
    
    def delNode(self, info):
        temp = self
        if temp.info == info:
            print('found')
            hold = temp
    
    def printTree(self):
        temp = self
        if temp.left:
            temp.left.printTree()
        print(temp.info),
        if temp.right:
            temp.right.printTree()
    
    def addNode(self, info):
        if self == None:
            self = Tree(info)
        temp = self
        if info < temp.info:
            if temp.left:
                temp = temp.left
                temp.addNode(info)
            else:
                temp.left = Tree(info)
        else:
            if temp.right:
                temp = temp.right
                temp.addNode(info)
            else:
                temp.right = Tree(info)

t = Tree(5)
t.addNode(3)
t.addNode(1)
t.addNode(11)
t.addNode(16)
t.addNode(12)
t.addNode(9)
t.printTree()