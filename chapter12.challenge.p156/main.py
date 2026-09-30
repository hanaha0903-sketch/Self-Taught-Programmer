import math

class Apple:
    def __init__(self, color, weight, size, price):
        self.color = color
        self.weight = weight
        self.size = size
        self.price = price
        print(f"Apple created: {self.color}, {self.weight}g, {self.size}, ${self.price}")

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.area = self.calculate_area()
        print(f"Circle created: radius={self.radius}, area={self.area}")

    def calculate_area(self):
        return math.pi * (self.radius ** 2)       
    
class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
        self.area = self.calculate_area()
        print(f"Triangle created: base={self.base}, height={self.height}, area={self.area}")

    def calculate_area(self):
        return 0.5 * self.base * self.height

class Hexagon:
    def __init__(self, side_length):
        self.side_length = side_length
        self.perimeter = self.calculate_perimeter()
        print(f"Hexagon created: side_length={self.side_length}, perimeter={self.perimeter}")

    def calculate_perimeter(self):
        return 6 * self.side_length
    
orange = Apple("orange", 150, "medium", 0.5)
circle = Circle(5)
triangle = Triangle(10, 5)
hexagon = Hexagon(4)

print(orange)
print(circle)
print(triangle)
print(hexagon)