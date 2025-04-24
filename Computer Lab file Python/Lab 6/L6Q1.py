print("Name:ARNAV JAIN")
print("Roll no.:24BEE162")
names= [("Rahul",), ("Danish",), "Shruti", "Shreya", ("Perry",), "Kohaku"]
boys = 0
girls = 0
print(names)
for name in names :
    if isinstance(name, tuple):
        boys += 1
    elif isinstance(name, str):
        girls += 1
print(f"Number of boys: {boys}")
print(f"Number of girls: {girls}")
