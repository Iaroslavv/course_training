from base import Figure

class Triangle(Figure):
    def __init__(self, first_side, second_side, third_side):
        self.first_side = first_side
        self.second_side = second_side
        self.third_side = third_side
        super().__init__('triangle')
    
    @property
    def area(self):
        area = (self.first_side + self.second_side + self.third_side) / 2
        return (area*(area-self.first_side)*(area-self.second_side)*(area-self.third_side)) ** 0.5 
    
    @property
    def perimeter(self):
        return int(self.first_side + self.second_side + self.third_side)
