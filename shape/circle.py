from .shape import Figure
from math import pi, pow


class Circle(Figure):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError(f"Окружность с радиусом: {radius}")

        self.radius = radius
        super().__init__()

    def get_area(self):
        return pi * pow(self.radius, 2)

    def get_perimeter(self):
        return 2 * pi * self.radius
