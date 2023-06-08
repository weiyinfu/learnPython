"""
在Python中，一切皆引用，这样会非常节省内存
"""
x = (1, 2, 3)
print(id(x))
a = [x, x, x]
b = []
b.append(a[0])  # 此处并不会复制一份新的元组
print(id(a[0]) == id(a[1]))
print(id(a[0]) == id(b[0]))

"""
demo2：一切皆引用
"""
x = [1, 2, 3]
b = []
b.append(x)
b[0][0] = 100
print(x)
