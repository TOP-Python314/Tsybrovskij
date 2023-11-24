def rook_move(start_cell,end_cell):
	start_letter=start_cell[0]
	start_num=int(start_cell[1])
	end_letter=end_cell[0]
	end_num=int(end_cell[1])	
	if ord(start_cell[0])>ord('h') or int(start_cell[1])>8:
		return "Ошибка позиции!!!"
	elif ord(end_cell[0])>ord('h') or int(end_cell[1])>8:
		return "Ошибка позиции!!!"
	elif start_letter==end_letter or start_num==end_num:
		return "Да"
	else:
		return "Нет"

start=input("Введите стартовую позицию:").lower()
move=input("Введите следующую позицию:").lower()
end_move=rook_move(start,move)
print(end_move)
# Немнога подкорректировал для себя, то бишь добавил проверку позиции.
# Введите стартовую позицию:a1
# Введите следующую позицию:a5
# Да
# Введите стартовую позицию:a1
# Введите следующую позицию:b2
# Нет