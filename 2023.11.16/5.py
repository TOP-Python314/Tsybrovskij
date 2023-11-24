int_num=int(input('Введите целочисленое: '))
float_num=int(input('Введите целочисленое: '))
mill=float(f'{int_num}.{float_num}')
km=1.61
print(f'{mill} миль = {(mill*km):.1f} км')
# Введите целочисленое: 15
# Введите целочисленое: 7
# 15.7 миль = 25.3 км