from collections import defaultdict


def function():
    return "I don't know"


dic = defaultdict(function)
dic.update(dict(one=1, two=2, three=3))
print(dic['four'])
