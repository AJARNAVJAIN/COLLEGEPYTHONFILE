print("Name:ARNAV JAIN")
print("Roll no.:24BEE162")
class String:
    def __init__(self, value=""):
        """Initialize the String object with an initial value."""
        self.value = value

    def __str__(self):
        """Return the string representation of the String object."""
        return self.value

    def __iadd__(self, other):
        """Overloads the '+= operator' to concatenate strings."""
        if isinstance(other, String):
            self.value += other.value
        elif isinstance(other, str):
            self.value += other
        return self

    def toLower(self):
        """Convert all uppercase letters in the string to lowercase."""
        self.value = self.value.lower()

    def toUpper(self):
        """Convert all lowercase letters in the string to uppercase."""
        self.value = self.value.upper()

# Example usage
if __name__ == "__main__":
    str1 = String("Hello")
    str2 = String(" World")

    print(f"Initial String 1: {str1}")
    print(f"Initial String 2: {str2}")

    # Concatenate using overloaded '+=' operator
    str1 += str2
    print(f"After concatenation: {str1}")

    # Convert to lowercase
    str1.toLower()
    print(f"After converting to lowercase: {str1}")

    # Convert to uppercase
    str1.toUpper()
    print(f"After converting to uppercase: {str1}")
