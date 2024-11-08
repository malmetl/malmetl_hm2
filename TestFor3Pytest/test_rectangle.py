import pytest
from scr.Rectangle import Rectangle


def test_rectangle_area(rectangle):
    if isinstance(rectangle, Rectangle):
        assert rectangle.get_area == rectangle.side_a * rectangle.side_b


def test_rectangle_perimeter(rectangle):
    if isinstance(rectangle, Rectangle):
        assert rectangle.get_perimeter == 2 * (rectangle.side_a + rectangle.side_b)


@pytest.mark.parametrize("side_a, side_b", [(0, 5), ('three', 5), (3.5, 5)])
def test_invalid_rectangle(side_a,side_b):
    with pytest.raises(ValueError):
        Rectangle(side_a, side_b)