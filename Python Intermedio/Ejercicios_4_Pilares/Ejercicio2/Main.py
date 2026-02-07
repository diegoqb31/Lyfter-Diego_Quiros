from Circle import Circle
from Square import Square
from Rectangle import Rectangle

def Main():
    circle = Circle(5)
    print(f"Circulo con radio de {circle.radius}, perimetro de {circle.calculate_perimeter()} y area de {circle.calculate_area()}")
    
    square = Square(7)
    print(f"Cuadrado con lado de {square.side}, perimetro de {square.calculate_perimeter()} y area de {square.calculate_area()}")
    
    rectangle = Rectangle(8,5)
    print(f"Rectangulo con largo de {rectangle.length}, un ancho de {rectangle.width} perimetro de {rectangle.calculate_perimeter()} y area de {rectangle.calculate_area()}")
    
Main()

