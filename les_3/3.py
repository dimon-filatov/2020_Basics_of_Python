# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(x, y, z):
    my_list = [x, y, z]
    my_list.remove(min(my_list))
    return sum(my_list)

print(my_func(12, 11, 11))
