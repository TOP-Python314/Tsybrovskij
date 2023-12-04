n = int(input('Введите целое число: '))
div_sum = 0
for i in range(1, n//2 + 1):
	if n%i == 0:
		# print(i)
		div_sum += i
print(div_sum + n)

# Введите целое число: 50
# 93