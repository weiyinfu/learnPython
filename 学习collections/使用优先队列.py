from queue import PriorityQueue


def test1():
    q = PriorityQueue()
    import random

    for i in range(10):
        q.put(random.randint(0, 10))

    while q:
        try:
            print(q.get_nowait())
        except:
            break


def test2():
    # 优先队列自定义Node，但是不能给Node添加__lt__比较函数
    q = PriorityQueue()

    class Node:
        def __init__(self, v):
            self.value = v

        def __repr__(self):
            return f"Node({self.value})"

    import random
    a = [Node(random.randint(0, 10)) for i in range(10)]
    print(len(a))

    class MyQNode:
        def __init__(self, node):
            self.node = node

        def __lt__(self, other):
            return self.node.value < other.node.value

    for i in a:
        q.put(MyQNode(i))
    while not q.empty():
        res = q.get().node
        print(res)


test2()
