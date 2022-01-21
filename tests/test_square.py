import pytest

from src.base_class import Figure
from src.square import Square

from helper_methods import check_group_is_int_instance

class TestSquare:
    
    def test_is_subclass(self):
        assert issubclass(Square, Figure) == True, 'Square is not a subclass of Figure'
    
    @pytest.mark.parametrize("side, expected", [(4, 16), (3, 9), (0, 0)])
    def test_area(self, side, expected):
        square = Square(side)
        check_group_is_int_instance(side)

        assert square.area == expected, f'Wrong area! Expected: {expected}, got {square.area}'

    @pytest.mark.parametrize("side, expected", [(3, 12), (5, 20), (0, 0)])
    def test_perimeter(self, side, expected):
        square = Square(side)
        check_group_is_int_instance(side)

        assert square.perimeter == expected, f'Wrong area! Expected: {expected}, got {square.area}'
    
    def test_adding_circle_area(self, square, circle):
        # 16 + 78.5
        assert square.add_area(circle) == 94.5, f"Total area of {square._name} and {circle._name} is incorrect."

    def test_adding_rectangle_area(self, square, rectangle):
        # 16 + 15
        assert square.add_area(rectangle) == 31, f"Total area of {square._name} and {rectangle._name} is incorrect."
    
    def test_adding_triangle_area(self, square, triangle):
        # 16 + 84
        assert square.add_area(triangle) == 100, f"Total area of {square._name} and {triangle._name} is incorrect."
