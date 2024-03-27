from .figure import Figure
from math import sqrt, pow


class Triangle(Figure):
    def __init__(self, side_1, side_2, side_3):
        self.s_1 = side_1
        self.s_2 = side_2
        self.s_3 = side_3

    def area(self):
        p = self.perimeter()
        return sqrt(
            p *
            (p-self.s_1) *
            (p-self.s_2) *
            (p-self.s_3)
        )

    def perimeter(self):
        return (
                       self.s_1 + self.s_2 + self.s_3
               ) / 2

    def is_right(self) -> bool:
        if self.s_1 > self.s_2:
            if self.s_1 > self.s_3:
                return pow(self.s_1, 2) == pow(self.s_2, 2) + pow(self.s_3, 2)
            return pow(self.s_3, 2) == pow(self.s_2, 2) + pow(self.s_1, 2)
        elif self.s_2 > self.s_3:
            return pow(self.s_3, 2) == pow(self.s_2, 2) + pow(self.s_1, 2)
        return pow(self.s_2, 2) == pow(self.s_1, 2) + pow(self.s_3, 2)
