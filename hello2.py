print ('words, yada yada yada'.upper())
print ('words, yada yada yada'.swapcase())

class MyString(str):
    def __str__(self):
        return self[::-1]

s = 'flea fly flo. {}'
t = MyString('the fellowship of the ring')
print (s.format(8*8))
print (t)