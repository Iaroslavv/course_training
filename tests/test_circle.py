import pytest

from src.circle import Circle
from src.base_class import Figure

from helper_methods import check_group_is_int_instance

class TestCircle:
    
    def test_is_subclass(self):
        assert issubclass(Circle, Figure) == True, 'Circle is not a subclass of Figure'

    @pytest.mark.parametrize("radius, expected", [(5, 78.5), (1, 3.14), (0, 0)])
    def test_area(self, radius, expected):
        circle = Circle(radius)
        check_group_is_int_instance(radius)

        assert circle.area == expected, f'Wrong area! Expected: {expected}, got {circle.area}'
    
    @pytest.mark.parametrize("radius, expected", [(5, 31.4), (1, 6.28), (0, 0)])
    def test_perimeter(self, radius, expected):
        circle = Circle(radius)
        check_group_is_int_instance(radius)
        
        assert circle.perimeter == expected, f'Wrong perimeter! Expected: {expected}, got {circle.perimeter}'
    
    def test_adding_rectangle_area(self, circle, rectangle):
        assert circle.add_area(rectangle) == 93.5, f"Total area of {circle._name} and {rectangle._name} is incorrect."
    
    def test_adding_square_area(self, circle, square):
        assert circle.add_area(square) == 94.5, f"Total area of {circle._name} and {square._name} is incorrect."
    
    def test_adding_triangle_area(self, circle, triangle):
        assert circle.add_area(triangle) == 162.5, f"Total area of {circle._name} and {triangle._name} is incorrect."
