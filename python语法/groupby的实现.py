from itertools import groupby

"""
python的groupby是一种O(n)复杂度的算法，它只会把连续的东西归为一组
例如groupby([1,2,1,2,3])，会得到五个group而不是3个group
如果想要实现真正的groupby，可以使用defaultdict

```
ma=defaultdict(lambda:[])
for i in a:
    ma[key(i)].append(i)
return ma
```
"""
a = [(1, 2, 3), (1, 3, 4), (2, 1, 3), (2, 3, 4), (1, 5, 6)]

b = groupby(a, key=lambda x: x[0])
for x, y in b:
    print(x, list(y))
print('==' * 10)
a = [1, 2, 1, 2, 3]
for x, y in groupby(a):
    print(x, list(y))
