from base import Figure

from math import pi

class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius
        self.pi = round(pi, 2)
        super().__init__('circle')
    
    @property
    def area(self):
        return self.pi * (self.radius ** 2)

    @property
    def perimeter(self):
        return self.radius * self.pi * self.radius
        