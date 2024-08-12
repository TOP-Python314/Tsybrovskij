list1 = list(input('Введите список: '))
list2 = list(input('Введите список: '))
if len(list1) < len(list2):
    list1, list2 = list2, list1

def check_sublist(list1, list2):
    if not list2:
        return 'Да'
    
    for i in range(len(list1) - len(list2) + 1):
        if list1[i:i + len(list2)] == list2:
            return 'Да'
    return 'Нет'

result = check_sublist(list1, list2)
print(result)

'''
Введите список: 1 2 3 4 5
Введите список: 3 4
Да

Введите список: 1 2 3 4 5
Введите список: 3 5
Нет

Введите список: 1 2 3 4 5
Введите список:
Да

Введите список:
Введите список: 1 2 3 4 5
Да
'''