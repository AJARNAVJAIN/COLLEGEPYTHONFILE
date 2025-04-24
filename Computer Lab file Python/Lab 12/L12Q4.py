print("Name:ARNAV JAIN")
print("Roll no.:24BEE162")
import math

class RegularShape:
    def __init__(self, shape, **kwargs):
        self.shape = shape.lower()
        self.kwargs = kwargs

    def perimeter(self):
        if self.shape == "circle":
            radius = self.kwargs.get("radius")
            if radius is not None:
                return 2 * math.pi * radius
            else:
                raise ValueError("Radius is required for circle perimeter.")
        
        elif self.shape == "square":
            side = self.kwargs.get("side")
            if side is not None:
                return 4 * side
            else:
                raise ValueError("Side length is required for square perimeter.")
        
        elif self.shape == "equilateral triangle":
            side = self.kwargs.get("side")
            if side is not None:
                return 3 * side
            else:
                raise ValueError("Side length is required for equilateral triangle perimeter.")
        
        elif self.shape == "regular pentagon":
            side = self.kwargs.get("side")
            if side is not None:
                return 5 * side
            else:
                raise ValueError("Side length is required for regular pentagon perimeter.")
        
        else:
            raise ValueError(f"Unknown shape: {self.shape}")

    def area(self):
        if self.shape == "circle":
            radius = self.kwargs.get("radius")
            if radius is not None:
                return math.pi * radius ** 2
            else:
                raise ValueError("Radius is required for circle area.")
        
        elif self.shape == "square":
            side = self.kwargs.get("side")
            if side is not None:
                return side ** 2
            else:
                raise ValueError("Side length is required for square area.")
        
        elif self.shape == "equilateral triangle":
            side = self.kwargs.get("side")
            if side is not None:
                return (math.sqrt(3) / 4) * side ** 2
            else:
                raise ValueError("Side length is required for equilateral triangle area.")
        
        elif self.shape == "regular pentagon":
            side = self.kwargs.get("side")
            if side is not None:
                return (math.sqrt(5 * (5 + 2 * math.sqrt(5))) / 4) * side ** 2
            else:
                raise ValueError("Side length is required for regular pentagon area.")
        
        else:
            raise ValueError(f"Unknown shape: {self.shape}")


# Example usage
if __name__ == "__main__":
    # Circle example
    circle = RegularShape(shape="circle", radius=5)
    print(f"Perimeter of Circle: {circle.perimeter()} units")
    print(f"Area of Circle: {circle.area()} square units")

    # Square example
    square = RegularShape(shape="square", side=4)
    print(f"Perimeter of Square: {square.perimeter()} units")
    print(f"Area of Square: {square.area()} square units")

    # Equilateral Triangle example
    equilateral_triangle = RegularShape(shape="equilateral triangle", side=6)
    print(f"Perimeter of Equilateral Triangle: {equilateral_triangle.perimeter()} units")
    print(f"Area of Equilateral Triangle: {equilateral_triangle.area()} square units")

    # Regular Pentagon example
    pentagon = RegularShape(shape="regular pentagon", side=7)
    print(f"Perimeter of Regular Pentagon: {pentagon.perimeter()} units")
    print(f"Area of Regular Pentagon: {pentagon.area()} square units")
