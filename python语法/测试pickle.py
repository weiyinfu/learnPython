import pickle
import numpy as np


class Node:
    def __init__(self):
        self.x = 2
        self.y = 1
        self.a = np.arange(3)


o = Node()
x = pickle.dumps(o)
print(x)
ans = pickle.loads(x)
print(ans)
ans.a[1] = 100
print(o.a)
