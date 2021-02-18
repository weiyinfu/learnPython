import collections

Edge = collections.namedtuple('Edge', ['src', 'des', 'value'])
a = Edge('beijing', 'shanghai', 3)
print(a)
print(isinstance(a, Edge))
print(isinstance(a, tuple))
print(a is Edge)
