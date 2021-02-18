import pickle


class Node:
    def __init__(self, age):
        self.name = 'haha'
        self.age = age

    def haha(self):
        print('haha')


# x = Node()
# pickle.dump(x, open('haha.pkl', 'wb'))
x = pickle.load(open('haha.pkl', 'rb'))
x.haha()
