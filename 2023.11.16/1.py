# ИСПОЛЬЗОВАТЬ везде: PEP 8 рекомендует добавлять пробелы вокруг бинарных операторов
first_name = input('Введите имя: ')
last_name = input('Введите фамилию: ')
age = int(input('Введите год рождения: '))
# ИСПРАВИТЬ: количество операций конкатенации избыточно
print(last_name, first_name + ', ', 2023 - age)
# КОММЕНТАРИЙ: явная конкатенация строк с помощью оператора + является относительно медленной операцией в Python
# КОММЕНТАРИЙ: оптимальнее будет использовать возможности встроенной функции print(), которая оптимизирована на низком уровне


# Введите имя: Владимир
# Введите фамилию: Цыбровский
# Введите год рождения: 2000
# Цыбровский Владимир, 23


# ИТОГ: хорошо, но можно лучше — 2/3


# КОММЕНТАРИЙ: PEP 8 — сборник рекомендаций по стилистическому оформлению Python кода — их стоит использовать для большего удобства чтения своего и чужого кода: https://peps.python.org/pep-0008/

