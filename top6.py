from collections import deque

dq = deque()

choice = input("Qayerdan (chap/o`ng): ")
value = int(input("Qo`shiladigan sonni: "))

if choice.lower() == "chap":
    dq.appendleft(value)
elif choice.lower() == "o`ng" or choice.lower() == "ong":
    dq.append(value)
else:
    print("Noto`g`ri tanlov!")

print("Deque:", dq)