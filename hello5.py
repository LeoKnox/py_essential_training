class wizard:
    def __init__(self, n):
        self._n = n
    def __repr__(self):
        return f'the number of wizard is {self._n}'
    def __str__(self):
        return f'str: number {self._n}'
s = 'Type something here.'

t = wizard(99)
print(repr(t))
print(t)
print(ascii(t))
print(chr(128406))
print(ord('🖖'))