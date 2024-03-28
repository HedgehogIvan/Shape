from .figure import Figure
from math import pi, pow


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius
        super().__init__()

    def get_area(self):
        return pi * pow(self.radius, 2)

    def get_perimeter(self):
        return 2 * pi * self.radius
