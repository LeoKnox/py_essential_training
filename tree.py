class node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.head = None

    def printTree(self):
        if self.head.left:
            print('ll')
            self.head.left.printTree()
        print(self.head.info),
        if self.head.right:
            self.head.right.printTree()
    
    def addNode(self, info):
        if self.head == None:
            self.head = node(info)
            return
        temp = self.head
        while temp:
            if info < temp.info:
                print('left')
                print (f'info {info} and {temp.info}')
                if temp.left == None:
                    temp.left = node(info)
                    return
                else:
                    print('else')
                    temp = temp.left
            else:
                print ('right')
                if temp.right == None:
                    temp.right = node(info)
                    return
                else:
                    print('else')
                    temp = temp.right
            

t = Tree()
t.addNode(6)
t.addNode(3)
t.addNode(1)
t.printTree()
n = ()