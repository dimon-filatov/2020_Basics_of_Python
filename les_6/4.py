"""
4. Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""

import random


class Car:
    def __init__(self, color, name, speed=0, is_police=False):
        self.color = color
        self.name = name
        self._speed = speed
        self._is_police = is_police

    def go(self):
        self._speed = random.randint(1, 120)
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')
        self._speed = 0

    def turn(self, direction):
        print(f'Машина повернула в {direction}')

    def show_speed(self):
        print(f'Скорость {self._speed} км/ч')


class TownCar(Car):
    def show_speed(self):
        print(f'Скорость {self._speed} км/ч')
        if self._speed > 60:
            print('ПРЕВЫШЕНИЕ СКОРОСТИ!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print(f'Скорость {self._speed} км/ч')
        if self._speed > 40:
            print('ПРЕВЫШЕНИЕ СКОРОСТИ!')


class PoliceCar(Car):
    pass


print('car_1')
car_1 = PoliceCar('Белая', 'Лада', 30, is_police=True)
car_1.show_speed()
print()
print('car_2')
car_2 = WorkCar('Синяя', 'Газель', 95)
car_2.show_speed()
print()
print('car_3')
car_3 = TownCar('Красная', 'Вольво', 113)
car_3.show_speed()
car_3.turn('лево')
car_3.stop()
car_3.show_speed()
car_3.go()
car_3.show_speed()
