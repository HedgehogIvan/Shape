from .base import ConvexPolygon
from math import sqrt, pow, degrees, acos


class Triangle(ConvexPolygon):
    def __init__(self, side1, side2, side3):
        super().__init__(*self.__convert_to_polygon(side1, side2, side3))

    def get_area(self):
        semi_p = self.get_perimeter() / 2
        area = sqrt(
            semi_p *
            (semi_p - self.sides[0]) *
            (semi_p - self.sides[1]) *
            (semi_p - self.sides[2])
        )
        return area

    def get_perimeter(self):
        return sum(self.sides)

    def is_right(self) -> bool:
        """
        Метод для определения, является ли треугольник прямоугольным
        :return: True, если является False, если нет
        """
        s1 = self.sides[0]
        s2 = self.sides[1]
        s3 = self.sides[2]
        pow_s1 = pow(self.sides[0], 2)
        pow_s2 = pow(self.sides[1], 2)
        pow_s3 = pow(self.sides[2], 2)

        if s1 > s2 and s1 > s3:
            return pow_s1 == pow_s2 + pow_s3
        elif s2 > s1 and s2 > s3:
            return pow_s2 == pow_s1 + pow_s3
        else:
            return pow_s3 == pow_s1 + pow_s2

    def __convert_to_polygon(
            self,
            side1: (int|float),
            side2: (int|float),
            side3: (int|float)
    ) -> tuple[list[int|float], list[int|float]]:
        """
        Метод для преобразования параметров для создания треугольников в параметры выпуклого многоугольника
        :param side1: 1-ая сторона треугольника
        :param side2: 2-ая сторона треугольника
        :param side3: 3-ья сторона треугольника
        :return: tuple
        """
        sides = [side1, side2, side3]

        ang_1 = degrees(acos(
            (pow(side1, 2) + pow(side2, 2) - pow(side3, 2)) / (2 * side1 * side2)
        ))
        ang_2 = degrees(acos(
            (pow(side2, 2) + pow(side3, 2) - pow(side1, 2)) / (2 * side2 * side3)
        ))
        ang_3 = degrees(acos(
            (pow(side1, 2) + pow(side3, 2) - pow(side2, 2)) / (2 * side1 * side3)
        ))

        angles = [ang_1, ang_2, ang_3]
        return sides, angles