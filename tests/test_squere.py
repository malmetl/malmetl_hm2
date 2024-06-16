from scr.Square import Square
import pytest


def test_square_area(square):
    if isinstance(square, Square):
        assert square.get_area == square.side_a * square.side_a


def test_square_perimeter(square):
    if isinstance(square, Square):
        assert square.get_perimeter == 4 * square.side_a


def test_invalid_square():
    with pytest.raises(ValueError):
        Square(-3)
    with pytest.raises(ValueError):
        Square('four')
    with pytest.raises(ValueError):
        Square(4.5)
