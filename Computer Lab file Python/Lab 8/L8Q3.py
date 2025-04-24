print("Name:ARNAV JAIN")
print("Roll no.:24BEE162")
def modify_set():
    name_set = set()
    name_set.update(["Arnav", "Rahul", "Priya", "Neha", "Amit"])
    print(f"Initial Set: {name_set}")
    
    name_set.discard("Rahul")  # Remove an existing name
    name_set.discard("Priya")  # Remove another name
    name_set.add("Rohan")  # Add a new name
    print(f"Modified Set: {name_set}")

modify_set()
