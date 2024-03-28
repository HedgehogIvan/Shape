from .figure import Figure
from math import pi, pow


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * pow(self.radius, 2)

    def perimeter(self):
        return 2 * pi * self.radius
