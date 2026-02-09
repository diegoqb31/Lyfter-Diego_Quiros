from Shape import Shape
import math

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
    
    
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)
    
    
    def calculate_area(self):
        return self.width * self.length