"""
6. Необходимо создать (не программно) текстовый файл,
где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""


with open('hw6.txt', encoding='utf-8') as f_hw:
    data = f_hw.readlines()
result = {}
for line in data:
    element = line.split(':')
    study_hours = element[1].strip().split()
    hours = 0
    for i in study_hours:
        i = i.split('(')
        if i[0] == '—':
            pass
        else:
            hours += int(i[0])
    result[element[0]] = hours
print(result)
