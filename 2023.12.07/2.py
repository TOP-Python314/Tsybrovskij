fruits_list = []
key = True

while key == True:
    fruit = input('Введите название фрукта: ')
    if fruit == '':
        break
    fruits_list.append(fruit)

if len(fruits_list) > 1:
    print(', '.join(fruits_list[:-1]), 'и', fruits_list[-1])
else:
    print(fruits_list[0])

'''
Введите название фрукта: яблоко
Введите название фрукта: груша
Введите название фрукта: апельсин
Введите название фрукта: лимон
Введите название фрукта:
яблоко, груша, апельсин и лимон
'''