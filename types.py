from decimal import *

a = Decimal('.10')
b = Decimal('.30')
c = a + a + a - b

x = None
y = 7
z = 7.0
s = '7.0'
e = True

t = 'seven'.capitalize()
u = ''' 
-------
seven
-------
'''

print ('t is {1} and {0}'.format(t, u))
print ('numbers is {1:<09} and {0:>08}'.format(y, z))
print(type(t))