x = (1, 'two', 3.0, [4, 'four'], 5)
y = (1, 'two', 3.0, [4, 'four'], 5)
print('x is {}'.format(x))
print(type(x[1]))
print(id(x))
print(id(y))

if x[0] is y[0]:
    print('yes')
else:
    print('no')

if isinstance(x, tuple):
    print("yeah")
else:
    print("nah")