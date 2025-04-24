print("Name:ARNAV JAIN")
print("Roll no.:24BEE162")
import csv

# Define CSV filename
filename = 'excel_data.csv'

# Sample data to write
header = ['ID', 'Name', 'Department', 'Salary']
data = [
    [1, 'Alice Johnson', 'HR', 50000],
    [2, 'Bob Smith', 'Engineering', 75000],
    [3, 'Charlie Lee', 'Marketing', 62000],
    [4, 'Dana Kim', 'Finance', 67000]
]

# Write data to CSV
with open(filename, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # Write header
    writer.writerow(header)
    
    # Write rows
    writer.writerows(data)

print(f"CSV file '{filename}' created successfully. You can open it directly in MS-Excel.")
