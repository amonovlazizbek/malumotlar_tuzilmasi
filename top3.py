from collections import deque

text = input("Matn kiriting: ")

text = text.replace(" ", "").lower()

dq = deque(text)

is_palindrome = True

while len(dq) > 1:
    if dq.popleft() != dq.pop():
        is_palindrome = False
        break

if is_palindrome:
    print("Bu palindrom")
else:
    print("Bu palindrom emas")