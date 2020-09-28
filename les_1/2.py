# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.
time_input = int(input('Введи время в секундах >>>'))
hours = time_input // 3600
minutes = time_input // 60 % 60
seconds = time_input % 60
if hours > 24:
    hours %= 24
if len(str(hours)) == 1:
    hours = '0' + str(hours)
if len(str(minutes)) == 1:
    minutes = '0' + str(minutes)
if len(str(seconds)) == 1:
    seconds = '0' + str(seconds)

print(f'{hours}:{minutes}:{seconds}')
