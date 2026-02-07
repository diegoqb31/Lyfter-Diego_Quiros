from abc import ABC, abstractmethod

class Shape:
    
    def __init__(self):
        pass
    
    
    @abstractmethod
    def calculate_perimeter(self):
        pass
    
    
    @abstractmethod
    def calculate_area(self):
        pass