'''
6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах.
Реализовать словарь, в котором каждый ключ — характеристика товара, например название,
а значение — список значений-характеристик, например список названий товаров.
Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}'''

products = [
    (1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'ед': 'шт.'}),
    (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'ед': 'шт.'}),
    (3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'ед': 'шт.'})
]


i = 1
decisions = ['y', 'n', 'q']
result = {'название': [], 'цена': [], 'количество': [], 'ед': []}
for product in products:
    print('Хотите ли вы добавить в итоговые данные')
    print(product)
    while True:
        decision = input('"y" - да, "n" - нет, "q" - выход >>> ').lower()
        if decision not in decisions:
            print('Вы ввели не верное значение')
        else:
            break
    if decision == 'y':
        result['название'].append(product[1]['название'])
        result['цена'].append(product[1]['цена'])
        result['количество'].append(product[1]['количество'])
        result['ед'].append(product[1]['ед'])
    elif decision == 'n':
        pass
    else:
        break
print(result)