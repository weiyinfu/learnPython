"""
python中array和dict都是可以直接判断是否相等的
"""
a = {
    'one': 1,
    'two': [2, 3],
}
b = {
    'two': [2, 3],
    'one': 1,
}
print(a == b)
