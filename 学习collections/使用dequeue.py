from collections import deque

q = deque([1, 2, 3])
print(q)
q.appendleft(0)
q.append(4)
print(q)
q.pop()
q.popleft()
print(q)
