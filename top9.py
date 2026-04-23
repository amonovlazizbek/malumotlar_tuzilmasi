from collections import deque

text = input("Matn kiriting: ")

dq = deque()

for ch in text:
    dq.appendleft(ch)

reversed_text = ""

while dq:
    reversed_text += dq.pop()

print("Teskari matn:", reversed_text)