numbers = []
while True:
	number = int(input('Введите целое число:'))
	if number%7 == 0:
		numbers.append(number)
	else:
		print(' '.join(map(str, reversed(numbers))))
		break

# Введите целое число:7
# Введите целое число:7
# Введите целое число:7
# Введите целое число:14
# Введите целое число:21
# Введите целое число:23
# 21 14 7 7 7