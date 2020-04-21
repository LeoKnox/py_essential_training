class Tree:
    def __init__(self, info):
        self.left = None
        self.right = None
        self.info = info
    
    def delNode(self, info):
        if self== None:
            return False
        if self.info == info:
            if self.left.info == info and self.right.info == None:
                self = None
                return True
            elif self.left and self.right == None:
                self = self.left
                return True
            elif self.left == None and self.right:
                self = self.right
                return True

            self.left = None
    
    def addNode(self, info):
        if info < self.info:
            if self.left:
                return self.left.addNode(info)
            else:
                self.left = Tree(info)
        else:
            if self.right:
                return self.right.addNode(info)
            else:
                self.right = Tree(info)
    
    def traceTree(self):
        if self.left:
            self.left.traceTree()
        print( self.info),
        if self.right:
            self.right.traceTree()
    
    def delTree(self):
        self == None

t = Tree(7)
t.addNode(3)
t.addNode(10)
t.addNode(99)
t.addNode(23)
t.addNode(4)
t.addNode(1)
t.addNode(2)
t.addNode(77)
t.addNode(77)
t.addNode(76)
t.addNode(3)
t.addNode(43)
t.addNode(9)
t.traceTree()