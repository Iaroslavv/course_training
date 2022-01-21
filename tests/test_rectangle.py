import pytest

from src.base_class import Figure
from src.rectangle import Rectangle

from helper_methods import check_group_is_int_instance

class TestRectangle:
    
    def test_is_subclass(self):
        assert issubclass(Rectangle, Figure) == True, 'Rectangle is not a subclass of Figure'
    
    @pytest.mark.parametrize("length, width, expected", [(2, 5, 10), (3, 7, 21), (10, 0, 0)])
    def test_area(self, length, width, expected):
        rectangle = Rectangle(length, width)
        check_group_is_int_instance(length, width)

        assert rectangle.area == expected, f'Wrong area! Expected: {expected}, got {rectangle.area}'
    
    @pytest.mark.parametrize("length, width, expected", [(2, 5, 14), (3, 7, 20), (10, 0, 20)])
    def test_perimeter(self, length, width, expected):
        rectangle = Rectangle(length, width)
        check_group_is_int_instance(length, width)

        assert rectangle.perimeter == expected, f'Wrong area! Expected: {expected}, got {rectangle.area}'
    
    def test_adding_circle_area(self, rectangle, circle):
        assert rectangle.add_area(circle) == 93.5, f"Total area of {rectangle._name} and {circle._name} is incorrect."

    def test_adding_square_area(self, rectangle, square):
        # 15 + 16
        assert rectangle.add_area(square) == 31, f"Total area of {rectangle._name} and {square._name} is incorrect."
    
    def test_adding_triangle_area(self, rectangle, triangle):
        # 15 + 84
        assert rectangle.add_area(triangle) == 99, f"Total area of {rectangle._name} and {triangle._name} is incorrect."
        