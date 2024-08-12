def find_mail(mail):
    at_index = mail.find('@')
    if at_index == -1:
        return 'Нет'
    dot_index = mail.find('.', at_index)
    if dot_index == -1 or dot_index in (at_index + 1, len(mail) - 1):
        return 'Нет'
    return 'Да'
    
mail = input('Введите почту:')
result = find_mail(mail)
print (result)

'''
Введите почту:asdasd@afda.
Нет

Введите почту:asdasd@a.re
Да
'''