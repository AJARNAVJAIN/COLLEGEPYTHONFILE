print("Name:ARNAV JAIN")
print("Roll no.:24BEE162")
s = input("Enter a string: ")
i = 0
l = len(s)
count = 0
while i < l:
    if s[i] in 'aeiouAEIOU':
        count += 1
    i += 1
print(f"The string has {count} vowels")

