from .figure import Figure
from math import pi, pow


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = pi * pow(self.radius, 2)
        return area
