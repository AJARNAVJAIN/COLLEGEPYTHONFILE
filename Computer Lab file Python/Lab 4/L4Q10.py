print("Name:ARNAV JAIN")
print("Roll no.:24BEE162")
n = int(input("Enter a number:"))
a = 0
b = 1
print(a)
print(b)
for i in range(2, n):
        c = b
        b = b + a
        a = c
        print(b)
