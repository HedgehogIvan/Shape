from math import sin, pow, pi
from .base import ConvexPolygon


class Rhombus(ConvexPolygon):
    def __init__(self, side, angle):
        super().__init__(
            *self._convert_to_polygon(side, angle)
        )

    def get_area(self):
        return round(pow(self.sides[0], 2) * sin(self.angles[0] * pi / 180), 3)

    def _convert_to_polygon(self, side, angle):
        sides = [side, side, side, side]
        angles = [angle, 180 - angle, angle, 180 - angle]
        return sides, angles
