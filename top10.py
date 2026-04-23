from collections import deque

dq = deque()

n = int(input("Nechta element kiritasiz: "))

for _ in range(n):
    value = input("Qiymat kiriting: ")
    priority = input("Prioritet (y/p): ")

    if priority.lower() == "yuqori" or priority.lower() == "y":
        dq.appendleft(value)  
    else:
        dq.append(value)       

print("Chiqish tartibi:")

while dq:
    print(dq.popleft(), end=" ")