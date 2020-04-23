class Tree:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
    
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
t.printTree()