print("Name:ARNAV JAIN")
print("Roll no.:24BEE162")
characters = input("Enter a string :")
f = {}
for character in characters :
    if character in f :
        f[character] += 1
    else :
        f[character] = 1
for keys,values in f.items() :
    print(f"{keys} : {values}")        
