print("Name:ARNAV JAIN")
print("Roll no.:24BEE162")
import openpyxl

# Load the workbook and select the first sheet
wb = openpyxl.load_workbook('students.xlsx')
sheet = wb.active

# Create a dictionary to store student data
students_dict = {}

# Skip the header row and iterate through the rest
for row in sheet.iter_rows(min_row=2, values_only=True):
    rollno, name, sub1, sub2, sub3 = row
    total = sub1 + sub2 + sub3
    students_dict[rollno] = {
        'Name': name,
        'Subject1': sub1,
        'Subject2': sub2,
        'Subject3': sub3,
        'Total': total
    }

# Display the dictionary
print("Student Records:\n")
for rollno, details in students_dict.items():
    print(f"Roll No: {rollno}")
    for key, value in details.items():
        print(f"  {key}: {value}")
    print("-" * 30)
