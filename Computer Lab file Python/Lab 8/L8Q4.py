print("Name:ARNAV JAIN")
print("Roll no.:24BEE162")
def separate_names():
    names_set = {"Amit", "Ankita", "Arjun", "Bobby", "Bhavesh", "Anurag", "Bina"}
    a_names = {name for name in names_set if name.startswith("A")}
    b_names = {name for name in names_set if name.startswith("B")}
    print(f"Names starting with A: {a_names}")
    print(f"Names starting with B: {b_names}")

separate_names()
