class Figure:
    def __init__(self, name):
        self._name = name
        if type(self) == Figure:
            raise Exception('FAILED to instantiate parent class! It must be subclassed.')
    
    def area(self):
        return 0
    
    def perimeter(self):
        return 0
    
    def add_area(self, figure_class):
        if figure_class._name in ('square', 'triangle', 'rectangle', 'circle'):
            return figure_class.area + self.area
        raise ValueError('Wrong class!')
