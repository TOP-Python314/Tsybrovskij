# ИСПОЛЬЗОВАТЬ везде: PEP 8 рекомендует добавлять пробелы вокруг бинарных операторов
int_num = int(input('Введите целочисленое: '))
float_num = int(input('Введите целочисленое: '))
mill = float(f'{int_num}.{float_num}')
# ИСПОЛЬЗОВАТЬ везде: круглые скобки используются для литерала кортежа, изменения порядка вычисления выражений, вызова функций и записи составного выражения на нескольких строчках — больше нигде и никак
print(f'{mill} миль = {mill * 1.61:.1f} км')


# Введите целочисленое: 15
# Введите целочисленое: 7
# 15.7 миль = 25.3 км


# ИТОГ: очень хорошо — 4/5
