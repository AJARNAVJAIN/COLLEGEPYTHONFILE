print("Name:ARNAV JAIN")
print("Roll no.:24BEE162")
def create_vcard():
    # Accept contact details from the user
    name = input("Enter Full Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    # Create vCard format string
    vcard = f"""BEGIN:VCARD
VERSION:3.0
FN:{name}
TEL;TYPE=CELL:{phone}
EMAIL;TYPE=INTERNET:{email}
ADR;TYPE=HOME:;;{address}
END:VCARD
"""

    # Save to .vcf file
    filename = name.replace(" ", "_") + ".vcf"
    with open(filename, "w") as f:
        f.write(vcard)

    print(f"\n✅ vCard saved as '{filename}' - You can now share it or open it on your phone.")

# Call the function
create_vcard()
print("Name:FARAZ HARADWALA")
print("Roll no.:24BEE168")
