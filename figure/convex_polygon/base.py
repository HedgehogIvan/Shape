from ..figure import Figure


class ConvexPolygon(Figure):
    """
    Класс для обозначения выпуклого многоугольника
    """
    def __init__(self, sides: list[int|float], angles: list[int|float]):
        if len(sides) < 3:
            raise ValueError('В многоугольнике не может быть меньше трёх сторон')

        if len(sides) != len(angles):
            raise ValueError('В многоугольнике кол-во углов не совпадает с кол-во сторон')

        self.sides = sides
        self.angles = angles

        self._catch_wrong_sides_value(self.sides)
        self._catch_wrong_angles_value(self.angles)

        super().__init__()

    def _catch_wrong_sides_value(self, sides: list[int|float]):
        """
        Метод отлова ошибок для значений сторон многоугольника
        В многоугольнике длина стороны должны быть:
        1. Больше нуля
        2. Меньше чем сумма других сторон многоугольника
        :param sides: список сторон многоугольника
        :return: вызывает ошибку, если какое-то из правил нарушено
        """
        # Пришлось разделить проверки на отрицательные стороны и сумму сторон
        # Так как есть вариации, когда при отрицательной стороне раньше срабатывает ошибка с суммой сторон
        for side in sides:
            if side <= 0:
                raise ValueError('Сторона многоугольника должна быть больше нуля')

        for i, side in enumerate(sides):
            if self._check_sum_sides_error(i, sides):
                raise ValueError(
                    'В многоугольнике есть сторона, которая больше суммы остальных её сторон. '
                    'Такой многоугольник существовать не может.'
                )

    def _check_sum_sides_error(self, index: int, sides: list[int|float]) -> bool:
        """
        Метод проверяет, больше ли сторона многоугольника суммы остальных её сторон
        :param index: Индекс проверяемой стороны
        :param sides: Список сторон
        :return: True, если сторона больше суммы остальных сторон
        """
        copy_sides = sides.copy()
        side = copy_sides.pop(index)
        if side >= sum(copy_sides):
            return True
        return False

    def _catch_wrong_angles_value(self, angles: list[int|float]):
        """
        Метод для отлова ошибок, связанных с углами многоугольника
        :param angles: Список углов в многоугольнике
        :return: вызывает ошибку, если какие-то из правил многоугольника нарушены
        """
        n = len(angles)
        convex_sum_angles = 180 * (n - 2)

        for angle in angles:
            if angle >= 180 or angle <= 0:
                raise ValueError(f'В выпуклом многоугольнике не может быть угла со значением: {angle}')

        diff_angles = convex_sum_angles - sum(angles)

        if round(diff_angles, 0) != 0:
            raise ValueError(
                f'Сумма углов в многоугольнике ({sum(angles)}) не равна необходимому значению ({convex_sum_angles})'
            )

    def _convert_to_polygon(self, **params):
        """
        Метод для преобразования параметров, необходимых для фигуры
        в параметры для многоугольника и его методов
        :param params: Параметры фигуры
        :return: Параметры многоугольника
        """
        pass