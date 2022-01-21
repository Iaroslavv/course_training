from src.base_class import Figure

from math import pi

class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius
        self.pi = round(pi, 2)
        super().__init__('circle')
    
    @property
    def area(self):
        return round(self.pi * (self.radius ** 2), 2)

    @property
    def perimeter(self):
        return round(2 * self.pi * self.radius, 2)
