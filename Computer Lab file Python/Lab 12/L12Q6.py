print("Name:ARNAV JAIN")
print("Roll no.:24BEE162")
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        """Returns a string representation of the date."""
        return f"{self.day:02}/{self.month:02}/{self.year}"

    def __eq__(self, other):
        """Overloads the == operator to compare two Date objects."""
        if isinstance(other, Date):
            return (self.day == other.day) and (self.month == other.month) and (self.year == other.year)
        return False  # In case the comparison is made with an object that is not a Date instance

# Example usage
if __name__ == "__main__":
    date1 = Date(25, 12, 2023)
    date2 = Date(25, 12, 2023)
    date3 = Date(1, 1, 2024)

    print(f"Date 1: {date1}")
    print(f"Date 2: {date2}")
    print(f"Date 3: {date3}")

    # Comparing dates
    if date1 == date2:
        print("\nDate 1 is the same as Date 2.")
    else:
        print("\nDate 1 is not the same as Date 2.")

    if date1 == date3:
        print("\nDate 1 is the same as Date 3.")
    else:
        print("\nDate 1 is not the same as Date 3.")
