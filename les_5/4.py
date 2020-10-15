"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""


with open('hw4-1.txt', encoding='utf-8') as old_f:
    with open('hw4-2.txt', 'w', encoding='utf-8') as new_f:
        for line in old_f:
            line = line.split()
            if line[0] == 'One':
                line[0] = 'Один'
            elif line[0] == 'Two':
                line[0] = 'Два'
            elif line[0] == 'Three':
                line[0] = 'Три'
            else:
                line[0] = 'Четыре'
            new_f.write(' '.join(line) + '\n')
