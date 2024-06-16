import pytest
import math
from scr.Circle import Cirсle
from scr.Rectangle import Rectangle
from scr.Square import Square
from scr.Triangle import Triangle


@pytest.fixture(params=[3, 'three', 3.5])
def circle(request):
    param = request.param
    if isinstance(param, int):
        return Cirсle(radius=param, pi=math.pi)
    else:
        with pytest.raises(ValueError):
            Cirсle(radius=param, pi=math.pi)


@pytest.fixture(params=[(3, 5), ('three', 5), (3.5, 5)])
def rectangle(request):
    side_a, side_b = request.param
    if isinstance(side_a, int) and isinstance(side_b, int):
        return Rectangle(side_a, side_b)
    else:
        with pytest.raises(ValueError):
            Rectangle(side_a, side_b)


@pytest.fixture(params=[4, 'four', 4.5])
def square(request):
    param = request.param
    if isinstance(param, int):
        return Square(param)
    else:
        with pytest.raises(ValueError):
            Square(param)


@pytest.fixture(params=[(3, 4, 5), ('three', 4, 5), (3.5, 4, 5)])
def triangle(request):
    side1, side2, side3 = request.param
    if isinstance(side1, int) and isinstance(side2, int) and isinstance(side3, int):
        return Triangle(side1, side2, side3)
    else:
        with pytest.raises(ValueError):
            Triangle(side1, side2, side3)


@pytest.fixture
def db():
    print("\nStart db")
    yield
    print("\nEnd db")


@pytest.fixture
def api_server(db):
    print("\nStart API")
    side_a = 5
    side_b = 2
    yield side_a, side_b
    print("\nEnd API")
