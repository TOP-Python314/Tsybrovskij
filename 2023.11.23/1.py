num1=float(input('Введите первое число: '))
num2=float(input('Введите второе число: '))
num3=float(input('Введите третье число: '))
if num1<0:
	print(num2+num3)
elif num2<0:
	print(num1+num3)
elif num3<0:
	print(num1+num2)
else:
	print(num1+num2+num3)
# Введите первое число: 1
# Введите второе число: -2
# Введите третье число: 1
# 2.0