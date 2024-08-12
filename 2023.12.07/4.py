list1 = []

while True:
    items_info = input()
    if items_info == '':
        break
    space_index = items_info.find(' ')
    if space_index != -1:
        key = items_info[:space_index]
        value = items_info[space_index + 1:]
        list1.append((key, value))
dictate = dict(list1)
value_row = input()

def find_key(dictate, value):
    for key, val in dictate.items():
        if value == val:
            return key
    return '! value error !'

result = find_key(dictate, value_row)
print(result)

'''
Пример 1:
1004 ER_CANT_CREATE_FILE
1005 ER_CANT_CREATE_TABLE
1006 ER_CANT_CREATE_DB
1007 ER_DB_CREATE_EXISTS
1008 ER_DB_DROP_EXISTS
1010 ER_DB_DROP_RMDIR
1016 ER_CANT_OPEN_FILE
1022 ER_DUP_KEY

ER_DUP_KEY
1022

Пример 2:
1004 ER_CANT_CREATE_FILE
1005 ER_CANT_CREATE_TABLE
1006 ER_CANT_CREATE_DB
1007 ER_DB_CREATE_EXISTS
1008 ER_DB_DROP_EXISTS
1010 ER_DB_DROP_RMDIR
1016 ER_CANT_OPEN_FILE
1022 ER_DUP_KEY

CANT_OPEN_FILE
! value error !
'''