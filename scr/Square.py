from scr.Rectangle import Rectangle
from abc import ABC, abstractmethod


class Square(Rectangle):
    @abstractmethod
    def __init__(self, side_a):
        if side_a <= 0:
            raise ValueError('Square side_a must be positive integers')
        super().__init__(side_a, side_a)