def f1():
    print ('this is f1')

def m1(m):
    def m2():
        print('this is before function call')
        m()
        print('this is after function call')
    return m2

@f1 # makes decorator can only be called through wrapper m1()
def m3():
    print('this is f3')

z = m1(m3)
z()
f1()
x = f1
x()
#y = m1
#y() #cannot call m2 directly only through m1