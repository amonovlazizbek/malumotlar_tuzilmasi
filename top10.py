from collections import deque

dq = deque()

n = int(input("Nechta element kiritasiz: "))

for _ in range(n):
    value = input("Qiymat kiriting: ")
    pri = input(" yuqori (y): ")

    if pri.lower() == "yuqori" or pri.lower() == "y":
        dq.appendleft(value)  
    else:
        dq.append(value)       

while dq:
    print(dq.popleft(), end=" ")
