from collections import deque

dq = deque()

dq.appendleft(10)
dq.appendleft(20)
dq.appendleft(30)

dq.append(40)
dq.append(50)

print("Deque:", dq)