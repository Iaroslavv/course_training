import pytest

from src.circle import Circle
from src.rectangle import Rectangle
from src.square import Square
from src.triangle import Triangle

@pytest.fixture(scope='session')
def circle():
    circle = Circle(5)
    yield circle
    del circle

@pytest.fixture(scope='session')
def rectangle():
    rectangle = Rectangle(5, 3)
    yield rectangle
    del rectangle

@pytest.fixture(scope='session')
def square():
    square = Square(4)
    yield square
    del square

@pytest.fixture(scope='session')
def triangle():
    triangle = Triangle(13, 14, 15)
    yield triangle
    del triangle
