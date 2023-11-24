def definition_cell(cell):
	letter=cell[0]
	num=int(cell[1])
	if (ord(letter)%2==0 and num%2==0) or ((ord(letter)%2!=0 and num%2!=0)):
		return "Чёрный"
	else:
		return "Белый"

start=input("Введите стартовую позицию:").lower()
move=input("Введите следующую позицию:").lower()
if definition_cell(start)==definition_cell(move):
	print('Да')
else:
	print('Нет')
# Введите стартовую позицию:a1
# Введите следующую позицию:b2
# Да