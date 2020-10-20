"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__()для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix():
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        result = ''
        for line in self.matrix:
            result += ' '.join([str(i) for i in line]) + '\n'
        return result

    def __add__(self, other):
        if len(self.matrix) == len(other.matrix):
            for i, line in enumerate(self.matrix):
                if len(line) == len(other.matrix[i]):
                    for ind, el in enumerate(line):
                        self.matrix[i][ind] += other.matrix[i][ind]
                else:
                    return f'Размер матриц не совпадает'
        else:
            return f'Размер матриц не совпадает'
        return Matrix(self.matrix)


a = [[31, 22], [37, 43], [51, 86]]
b = [[-31, -22], [3, 7], [9, -86]]
c = [[123, 433, 234], [432, 245, 687]]

matrix1 = Matrix(a)
matrix2 = Matrix(b)
matrix3 = Matrix(c)
print(matrix1 + matrix3)
print(matrix3)
print(matrix1 + matrix2)
