import pytest

from src.base_class import Figure
from src.triangle import Triangle

from helper_methods import check_group_is_int_instance

class TestTriangle:
    
    def test_is_subclass(self):
        assert issubclass(Triangle, Figure) == True, 'Triangle is not a subclass of Figure'
    
    @pytest.mark.parametrize("first_s, second_s, third_s,  expected", [
        (13, 14, 15, 84), (8, 3, 6, 7.64), (10, 10, 10, 43.3)
        ])
    def test_area(self, first_s, second_s, third_s, expected):
        triangle = Triangle(first_s, second_s, third_s)
        check_group_is_int_instance(first_s, second_s, third_s)

        assert triangle.area == expected, f'Wrong area! Expected: {expected}, got {triangle.area}'

    @pytest.mark.parametrize("first_s, second_s, third_s,  expected", [
        (13, 14, 15, 42), (8, 3, 6, 17), (10, 10, 10, 30)
        ])
    def test_perimeter(self, first_s, second_s, third_s, expected):
        triangle = Triangle(first_s, second_s, third_s)
        check_group_is_int_instance(first_s, second_s, third_s)
        
        assert triangle.perimeter == expected, f'Wrong perimeter! Expected: {expected}, got {triangle.perimeter}'
    
    def test_adding_circle_area(self, triangle, circle):
        # 84 + 78.5
        assert triangle.add_area(circle) == 162.5, f"Total area of {triangle._name} and {circle._name} is incorrect."
    
    def test_adding_rectangle_area(self, triangle, rectangle):
        # 84 + 15
        assert triangle.add_area(rectangle) == 99, f"Total area of {triangle._name} and {rectangle._name} is incorrect."
    
    def test_adding_square_area(self, triangle, square):
        # 84 + 16
        assert triangle.add_area(square) == 100, f"Total area of {triangle._name} and {square._name} is incorrect."
