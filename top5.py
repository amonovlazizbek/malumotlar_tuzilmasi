from collections import deque

dq = deque([10, 20, 30, 40, 50])

while dq:
    print(dq.pop(), end=" ")