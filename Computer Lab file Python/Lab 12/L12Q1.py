print("Name:ARNAV JAIN")
print("Roll no.:24BEE162")
class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        return f"{self.real} + {self.imag}i" if self.imag >= 0 else f"{self.real} - {-self.imag}i"

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real_part, imag_part)

    def __truediv__(self, other):
        denominator = other.real ** 2 + other.imag ** 2
        if denominator == 0:
            raise ZeroDivisionError("Cannot divide by zero complex number")
        real_part = (self.real * other.real + self.imag * other.imag) / denominator
        imag_part = (self.imag * other.real - self.real * other.imag) / denominator
        return ComplexNumber(real_part, imag_part)

# Example usage
if __name__ == "__main__":
    c1 = ComplexNumber(4, 5)
    c2 = ComplexNumber(2, -3)

    print("Complex Number 1:", c1)
    print("Complex Number 2:", c2)

    print("\nAddition:       ", c1 + c2)
    print("Subtraction:    ", c1 - c2)
    print("Multiplication: ", c1 * c2)
    print("Division:       ", c1 / c2)
