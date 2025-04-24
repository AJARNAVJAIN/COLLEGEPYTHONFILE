print("Name:ARNAV JAIN")
print("Roll no.:24BEE162")
import random as r
a = [r.randint(1, 100) for _ in range(5) if r.randint(1, 100) % 2 !=0 ]
print(f"Generated list 1: {a}")
b = [r.randint(1, 100) for _ in range(4) if r.randint(1, 100) % 2 ==0 ]
print(f"Generated list 2: {b}")
a[3] = b
print(a)

a.sort()
print(a)
