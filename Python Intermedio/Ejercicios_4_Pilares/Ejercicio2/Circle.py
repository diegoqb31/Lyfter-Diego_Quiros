from Shape import Shape
import math

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
    
    
    def calculate_perimeter(self):
        return 2 * math.pi * self.radius
    
    
    def calculate_area(self):
        return math.pi * (self.radius * self.radius)