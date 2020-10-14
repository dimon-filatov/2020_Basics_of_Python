"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк
выполнить подсчет количества строк, количества слов в каждой строке.
"""

with open('hw2.txt') as f_hw:
    information = f_hw.readlines()
    print(f'В файле {len(information)} строк')
    for i, lines in enumerate(information):
        print(f'В строке №{i + 1} {len(lines.split())} слов')
