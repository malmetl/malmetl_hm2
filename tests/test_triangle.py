import pytest
from scr.Triangle import Triangle
import math


def test_triangle_area(triangle):
    if isinstance(triangle, Triangle):
        s = (triangle.side1 + triangle.side2 + triangle.side3) / 2
        assert math.isclose(triangle.get_area,
                            math.sqrt(s * (s - triangle.side1) * (s - triangle.side2) * (s - triangle.side3)),
                            rel_tol=1e-9)


def test_triangle_perimeter(triangle):
    if isinstance(triangle, Triangle):
        assert triangle.get_perimeter == triangle.side1 + triangle.side2 + triangle.side3


def test_invalid_triangle():
    with pytest.raises(ValueError):
        Triangle(1, 1, 3)
    with pytest.raises(ValueError):
        Triangle('three', 4, 5)
    with pytest.raises(ValueError):
        Triangle(3.5, 4, 5)