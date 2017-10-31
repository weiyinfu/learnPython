import collections

a = collections.Counter('aabc')
b = collections.Counter('bbcd')
print(a)
print(b)
print(a - b)
print(a + b)
print(a & b)
print(a | b)
