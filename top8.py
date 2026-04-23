from collections import deque

max_size = 4
dq = deque()

while True:
    value = input("Son kiriting (yoki 's'): ")
    
    if value == "stop" or value == 's':
        break
    
    if len(dq) >= max_size:
        print("Xatolik: tulgan!")
    else:
        dq.append(int(value))
        print("Hozirgi deque:", dq)