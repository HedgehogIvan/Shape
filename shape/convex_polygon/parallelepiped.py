from .base import ConvexPolygon
from math import pi, sin


class Parallelepiped(ConvexPolygon):
    def __init__(self, side_1, side_2, angle):
        super().__init__(
            *self._convert_to_polygon(side_1, side_2, angle)
        )

    def get_area(self):
        return round(self.sides[0] * self.sides[1] * sin(self.angles[0] * pi / 180), 3)

    def _convert_to_polygon(self, side_1, side_2, angle):
        sides = [side_1, side_2, side_1, side_2]
        angles = [angle, 180 - angle, angle, 180 - angle]
        return sides, angles