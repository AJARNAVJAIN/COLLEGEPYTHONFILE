print("Name:ARNAV JAIN")
print("Roll no.:24BEE162")
def f(n):
    r = 1
    for i in range(1, n + 1):
        r *= i
    return r
n = int(input("Enter a number:"))
print("The factorial is:",f(n))
