# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# для решения используйте цикл while и арифметические операции.

number = int(input('Введи число >>>'))
max = 0
while number > 0:
    numeral = number % 10
    if numeral > max:
        max = numeral
    number //= 10
print(max)
