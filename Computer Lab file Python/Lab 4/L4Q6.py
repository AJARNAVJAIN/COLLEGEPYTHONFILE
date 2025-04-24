print("Name:ARNAV JAIN")
print("Roll no.:24BEE162")
for h in range(24):
        if h == 0:
            print(f"12:00 midnight")
        elif h == 12:
            print(f"12:00 noon")
        elif h < 12:
            print(f"{h}:00 AM")
        else:
            print(f"{h - 12}:00 PM")
