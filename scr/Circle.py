from abc import ABC

from Figure import Figure
import math


class Cirсle(Figure, ABC):

    def __init__(self, radius, pi):
        self.radius = radius
        self.pi = pi

    @property
    def get_area(self):
        return math.pi * self.radius ** 2

    @property
    def get_perimeter(self):
        return 2 * self.pi * self.radius
