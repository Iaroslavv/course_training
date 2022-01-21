from src.base_class import Figure

class Square(Figure):
    def __init__(self, side):
        self.side = side
        super().__init__('square')
    
    @property
    def area(self):
        return self.side ** 2
    
    @property
    def perimeter(self):
        return self.side * 4
