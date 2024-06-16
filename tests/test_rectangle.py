import pytest
from scr.Rectangle import Rectangle


def test_rectangle_area(rectangle):
    if isinstance(rectangle, Rectangle):
        assert rectangle.get_area == rectangle.side_a * rectangle.side_b


def test_rectangle_perimeter(rectangle):
    if isinstance(rectangle, Rectangle):
        assert rectangle.get_perimeter == 2 * (rectangle.side_a + rectangle.side_b)


def test_invalid_rectangle():
    with pytest.raises(ValueError):
        Rectangle(0, 5)
    with pytest.raises(ValueError):
        Rectangle('three', 5)
    with pytest.raises(ValueError):
        Rectangle(3.5, 5)
