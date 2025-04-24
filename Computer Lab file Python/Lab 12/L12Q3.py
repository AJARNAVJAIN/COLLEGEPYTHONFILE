print("Name:ARNAV JAIN")
print("Roll no.:24BEE162")
import math

class Solid:
    def __init__(self, shape, **kwargs):
        self.shape = shape.lower()
        self.kwargs = kwargs

    def surface_area(self):
        if self.shape == "sphere":
            radius = self.kwargs.get("radius")
            if radius is not None:
                return 4 * math.pi * radius ** 2
            else:
                raise ValueError("Radius is required for sphere surface area.")
        
        elif self.shape == "cube":
            side = self.kwargs.get("side")
            if side is not None:
                return 6 * side ** 2
            else:
                raise ValueError("Side length is required for cube surface area.")
        
        elif self.shape == "cylinder":
            radius = self.kwargs.get("radius")
            height = self.kwargs.get("height")
            if radius is not None and height is not None:
                return 2 * math.pi * radius * (radius + height)
            else:
                raise ValueError("Radius and height are required for cylinder surface area.")
        
        else:
            raise ValueError(f"Unknown shape: {self.shape}")

    def volume(self):
        if self.shape == "sphere":
            radius = self.kwargs.get("radius")
            if radius is not None:
                return (4/3) * math.pi * radius ** 3
            else:
                raise ValueError("Radius is required for sphere volume.")
        
        elif self.shape == "cube":
            side = self.kwargs.get("side")
            if side is not None:
                return side ** 3
            else:
                raise ValueError("Side length is required for cube volume.")
        
        elif self.shape == "cylinder":
            radius = self.kwargs.get("radius")
            height = self.kwargs.get("height")
            if radius is not None and height is not None:
                return math.pi * radius ** 2 * height
            else:
                raise ValueError("Radius and height are required for cylinder volume.")
        
        else:
            raise ValueError(f"Unknown shape: {self.shape}")


# Example usage
if __name__ == "__main__":
    # Sphere example
    sphere = Solid(shape="sphere", radius=5)
    print(f"Surface Area of Sphere: {sphere.surface_area()} units²")
    print(f"Volume of Sphere: {sphere.volume()} units³")

    # Cube example
    cube = Solid(shape="cube", side=4)
    print(f"Surface Area of Cube: {cube.surface_area()} units²")
    print(f"Volume of Cube: {cube.volume()} units³")

    # Cylinder example
    cylinder = Solid(shape="cylinder", radius=3, height=7)
    print(f"Surface Area of Cylinder: {cylinder.surface_area()} units²")
    print(f"Volume of Cylinder: {cylinder.volume()} units³")
