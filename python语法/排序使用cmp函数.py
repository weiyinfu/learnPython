import numpy as np
import functools
"""
python中使用cmp函数
有些时候可以直接按照元素的key进行排序，有些时候可以按照cmp进行排序。  
使用cmp的时候很容易使用key，使用key的时候如果使用cmp则必须自定义一种新的类型wrapper
"""
a = list(np.random.randint(0, 10, 10))


def cmp(x, y):
    return x - y


print(a)
a.sort(key=functools.cmp_to_key(cmp))
print(a)
