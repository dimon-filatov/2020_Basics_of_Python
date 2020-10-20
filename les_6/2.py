"""
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу:
длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1см *число см толщины полотна.
Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
"""


class Road:
    def __init__(self, width, length):
        self._width = width
        self._length = length
        self._mass_per_sq_m = 25
        self._thickness = 5

    def weight_calculation(self):
        weight = self._width * self._length * self._mass_per_sq_m * self._thickness
        return f'Вам потребуется {round(weight / 1000, 2)} т. асфальта для дороги длиной {self._length} м. шириной {self._width} м.'


new_road = Road(float(input('Введите ширину дороги >>> ')), float(input('Введите длину дороги >>> ')))
print(new_road.weight_calculation())
