import json
"""
python中的json是无限长的
"""
a = json.dumps({'age': 2 ** 165})
print(2 ** 165)
print(a)