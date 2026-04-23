from collections import deque

dq = deque()

text = input("Harflar kiriting: ")

for i, ch in enumerate(text):
    if i % 2 == 0:
        dq.appendleft(ch)  
        print(f"{ch} chapdan:", dq)
    else:
        dq.append(ch)      
        print(f"{ch} o`ngdan:", dq)