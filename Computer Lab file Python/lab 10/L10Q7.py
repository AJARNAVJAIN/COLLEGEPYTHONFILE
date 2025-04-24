print("Name:ARNAV JAIN")
print("Roll no.:24BEE162")
import pickle
from datetime import date

# Step 1: Define the Employee class
class Employee:
    def __init__(self, empcode, empname, doj, salary):
        self.empcode = empcode
        self.empname = empname
        self.doj = doj  # Date of Joining (date object)
        self.salary = salary

    def display(self):
        print(f"Emp Code: {self.empcode}")
        print(f"Name: {self.empname}")
        print(f"Date of Joining: {self.doj}")
        print(f"Salary: {self.salary}")

# Step 2: Serialize the object
def serialize_employee(emp, filename):
    with open(filename, 'wb') as file:
        pickle.dump(emp, file)
    print(f"✅ Employee data serialized to '{filename}'")

# Step 3: Deserialize the object
def deserialize_employee(filename):
    with open(filename, 'rb') as file:
        emp = pickle.load(file)
    print(f"\n✅ Employee data deserialized from '{filename}':")
    emp.display()

# Example usage
if __name__ == "__main__":
    # Create an employee object
    emp = Employee(empcode="E101", empname="John Doe", doj=date(2021, 5, 10), salary=55000)

    # File to save serialized data
    file_name = "employee.dat"

    # Serialize
    serialize_employee(emp, file_name)

    # Deserialize
    deserialize_employee(file_name)
