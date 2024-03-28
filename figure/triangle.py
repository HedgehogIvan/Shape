from .figure import Figure
from math import sqrt, pow


class Triangle(Figure):
    def __init__(self, side_1, side_2, side_3):
        self.s_1 = side_1
        self.s_2 = side_2
        self.s_3 = side_3

        super().__init__()

    def area(self):
        semi_p = self.perimeter() / 2
        area = sqrt(
            semi_p *
            (semi_p - self.s_1) *
            (semi_p - self.s_2) *
            (semi_p - self.s_3)
        )
        return area

    def perimeter(self):
        return self.s_1 + self.s_2 + self.s_3

    def is_right(self) -> bool:
        pow_s1 = pow(self.s_1, 2)
        pow_s2 = pow(self.s_2, 2)
        pow_s3 = pow(self.s_3, 2)

        if self.s_1 > self.s_2 and self.s_1 > self.s_3:
            return pow_s1 == pow_s2 + pow_s3
        elif self.s_2 > self.s_1 and self.s_2 > self.s_3:
            return pow_s2 == pow_s1 + pow_s3
        else:
            return pow_s3 == pow_s1 + pow_s2
