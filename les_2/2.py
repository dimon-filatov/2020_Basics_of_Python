# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

print('Создай список данный, для выхода из создания списка, набери "exit"')
some_list = []
while True:
    new_one = input('Введи элемент списка >>>')
    if new_one != 'exit':
        some_list.append(new_one)
    else:
        break
print(some_list)
result = []
if some_list:
    for element in some_list[::2]:
        result.append(element)
    i = 0
    for element2 in some_list[1::2]:
        result.insert(i, element2)
        i += 2
print(result)