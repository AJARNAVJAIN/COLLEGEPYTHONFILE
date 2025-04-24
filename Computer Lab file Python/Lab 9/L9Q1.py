print("Name:ARNAV JAIN")
print("Roll no.:24BEE162")
def countLowerUpper(string):
    counts = {"upper":0,"lower":0}
    for i in string :
        if i.isupper():
            counts["upper"] += 1
        elif i.islower():
            counts["lower"] += 1
    return counts
string = input("Enter a string:")
print(countLowerUpper(string))
