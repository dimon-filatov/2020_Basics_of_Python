"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod


class Clothing(ABC):
    def __init__(self, data):
        self.data = data

    @abstractmethod
    def tissue_consumption(self):
        pass


class Coat(Clothing):
    @property
    def tissue_consumption(self):
        return round(self.data / 6.5 + 0.5, 2)


class Suit(Clothing):
    @property
    def tissue_consumption(self):
        return round(2 * self.data + 0.3, 2)


coat = Coat(100)
suit = Suit(1000)
print(coat.tissue_consumption)
print(suit.tissue_consumption)
