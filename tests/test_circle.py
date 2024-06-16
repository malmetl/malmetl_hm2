import pytest
import math
from scr.Circle import Cirсle


def test_circle_area(circle):
    if isinstance(circle, Cirсle):
        assert math.isclose(circle.get_area, math.pi * circle.radius ** 2)


def test_circle_perimeter(circle):
    if isinstance(circle, Cirсle):
        assert math.isclose(circle.get_perimeter, 2 * math.pi * circle.radius)


def test_invalid_circle_type():
    with pytest.raises(ValueError):
        Cirсle(radius='three', pi=math.pi)
    with pytest.raises(ValueError):
        Cirсle(radius=3.5, pi=math.pi)
