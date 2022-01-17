from base import Figure

class Rectangle(Figure):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        super().__init__('rectangle')
    
    @property
    def area(self):
        return self.length * self.width

    @property
    def perimeter(self):
        return (self.length + self.width) * 2
    
    @property
    def add_area(self, figure):
        pass
