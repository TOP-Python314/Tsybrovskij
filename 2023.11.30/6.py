ticket = input('Введите номер билета: ')
if len(ticket) != 6:
	print("Кол-во цифр не соответствуют билету!")
else:
	num1 = sum(map(int, ticket[:3]))
	num2 = sum(map(int, ticket[3:]))
	
	if num1 == num2:
		print('Да')
	else:
		print('Нет')

# Введите номер билета: 183534
# Да
# Введите номер билета: 401367
# Нет