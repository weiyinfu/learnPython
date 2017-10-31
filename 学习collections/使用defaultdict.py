from collections import defaultdict

dic = defaultdict(lambda: "I don't know", {'one': 1, 'two': 2, 'three': 3})
print(dic['four'])
