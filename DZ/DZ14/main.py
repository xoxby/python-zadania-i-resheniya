
# --- Задание 1 ---
import math


def calculate_area(figure_type, **kwargs):
    """
    Рассчитывает площадь геометрической фигуры.

    Параметры:
        figure_type: тип фигуры ('rhombus', 'square', 'trapezoid', 'circle')
        **kwargs: параметры фигуры (d1, d2, a, b, h, r)

    Возвращает:
        Площадь фигуры или строку 'invalid data'
    """
    if figure_type == 'rhombus':
        # Ромб: s = (d1 * d2) / 2
        d1 = kwargs.get('d1', 0)
        d2 = kwargs.get('d2', 0)
        return (d1 * d2) / 2

    elif figure_type == 'square':
        # Квадрат: s = a²
        a = kwargs.get('a', 0)
        return a ** 2

    elif figure_type == 'trapezoid':
        # Трапеция: s = ½ * (a + b) * h
        a = kwargs.get('a', 0)
        b = kwargs.get('b', 0)
        h = kwargs.get('h', 0)
        return 0.5 * (a + b) * h

    elif figure_type == 'circle':
        # Круг: s = π * r²
        r = kwargs.get('r', 0)
        return math.pi * r ** 2

    else:
        return "invalid data"


print(calculate_area('rhombus', d1=10, d2=8))       # 40.0
print(calculate_area('square', a=5))                  # 25
print(calculate_area('trapezoid', a=12, b=3, h=6))   # 45.0
print(calculate_area('circle', r=18))                  # 1017.8760197630929
print(calculate_area('unknown', a=1, b=2, c=3))       # invalid data
