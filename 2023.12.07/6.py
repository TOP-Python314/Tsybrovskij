def check_binar_string(n):
    binar_digit = {'0', '1'}
    
    if len(n) > 2 and n[0] == '0' and n[1] == 'b':
        n = n[2:]
    elif len(n) > 1 and n[0] == 'b':
        n = n[1:]
    
    for char in n:
        if char not in binar_digit:
            return 'Нет'
    return 'Да'

str_code = input().strip()
result = check_binar_string(str_code)
print(result)

'''
Примеры:
0b11001
Да

b11001
Да

1b1001
Нет
'''