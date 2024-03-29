from .base import ConvexPolygon


class Rectangle(ConvexPolygon):
    def __init__(self, side_1, side_2):
        super().__init__(
            *self._convert_to_polygon(side_1, side_2)
        )

    def area(self):
        return self.sides[0] * self.sides[1]

    def _convert_to_polygon(self, side_1, side_2):
        sides = [side_1, side_2, side_1, side_2]
        angles = [90, 90, 90, 90]
        return sides, angles
