from Shape import Shape
import math

class Square(Shape):
    def __init__(self, side):
        super().__init__()
        self.side = side
    
    
    def calculate_perimeter(self):
        return self.side * 4
    
    
    def calculate_area(self):
        return self.side * self.side