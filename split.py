s = 'This is a long string with extra words to make it even longer, it would not be long without useless words.'
l = s.split()
s2 = ":".join(l)
print(s2)
print(s.split())
print(s.split('i'))