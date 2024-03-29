from .base import ConvexPolygon
from math import sqrt, pow, degrees, acos


class Triangle(ConvexPolygon):
    def __init__(self, side1, side2, side3):
        super().__init__(
            *self._convert_to_polygon(
               side1, side2, side3
            )
        )

    def get_area(self):
        semi_p = self.get_perimeter() / 2
        area = sqrt(
            semi_p *
            (semi_p - self.sides[0]) *
            (semi_p - self.sides[1]) *
            (semi_p - self.sides[2])
        )
        return round(area, 3)

    def is_right(self) -> bool:
        """
        Метод для определения, является ли треугольник прямоугольным
        :return: True, если является False, если нет
        """
        s1, s2, s3 = self.sides
        pow_s1 = pow(s1, 2)
        pow_s2 = pow(s2, 2)
        pow_s3 = pow(s3, 2)

        if s1 > s2 and s1 > s3:
            return pow_s1 == pow_s2 + pow_s3
        elif s2 > s1 and s2 > s3:
            return pow_s2 == pow_s1 + pow_s3
        else:
            return pow_s3 == pow_s1 + pow_s2

    def _convert_to_polygon(
            self, side_1, side_2, side_3
    ) -> tuple[list[int|float], list[int|float]]:
        """
        Метод для преобразования параметров для создания треугольников в параметры выпуклого многоугольника
        :param side_1: Первая сторона треугольника
        :param side_2: Вторая сторона треугольника
        :param side_3: Третья сторона треугольника
        :return: tuple
        """
        sides = [side_1, side_2, side_3]
        s1, s2, s3 = side_1, side_2, side_3

        self._catch_wrong_sides_value(sides)

        # Генерация углов на основе сторон
        ang_1 = degrees(acos(
            (pow(s1, 2) + pow(s2, 2) - pow(s3, 2)) / (2 * s1 * s2)
        ))
        ang_2 = degrees(acos(
            (pow(s2, 2) + pow(s3, 2) - pow(s1, 2)) / (2 * s2 * s3)
        ))
        ang_3 = degrees(acos(
            (pow(s1, 2) + pow(s3, 2) - pow(s2, 2)) / (2 * s1 * s3)
        ))

        angles = [ang_1, ang_2, ang_3]
        return sides, angles