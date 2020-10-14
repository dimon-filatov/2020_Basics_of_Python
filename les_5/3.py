"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

with open('hw3.txt', encoding='utf-8') as f_hw:
    data = f_hw.readlines()

salary_fund = 0
print('У этих людей зарплата менее 20 000 руб:')
for line in data:
    person = line.strip().split()
    salary = float(person[1])
    salary_fund += salary
    if salary < 20000:
        print(person[0])
print(f'Общий зарплатный фонд {round(salary_fund, 2)}, средняя зарплата {round(salary_fund / len(data), 2)}')
