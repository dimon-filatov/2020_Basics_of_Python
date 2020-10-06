# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

numbers = []
print('Для выхода нажми введи "q"')
while True:
    user_input = input().lower()
    if user_input == 'q' or 'q' in user_input:
        if user_input == 'q':
            break
        else:
            result_list = user_input.split()
            result_list.remove('q')
            numbers.append(sum(list(map(int, result_list))))
            print(sum(numbers))
            break
    else:
        numbers.append(sum(list(map(int, user_input.split()))))
        print(sum(numbers))
