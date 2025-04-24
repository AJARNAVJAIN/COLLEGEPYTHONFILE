print("Name:ARNAV JAIN")
print("Roll no.:24BEE162")
def convert(string):
    a = string.split()
    b = []
    c = []
    for i in a :
        if i.isalpha():
            b.append(i)
        elif i.isdigit():
            c.append(i)

    print(b)
    print(c)
    d = sorted(b)
    e = sorted(c)
    f = e + d
    g = set[f]
    return g
string = input("Enter a string:")
print(convert(string))
