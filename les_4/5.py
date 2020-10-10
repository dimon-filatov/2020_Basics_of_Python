'''
5. Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
'''

import functools


def my_multiplication(x, y):
    return x * y


my_list = [i for i in range(100, 1001) if i % 2 == 0]
print(functools.reduce(my_multiplication, my_list))
