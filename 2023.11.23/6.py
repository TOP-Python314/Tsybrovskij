def king_move(start_cell,end_cell):
	start_letter=start_cell[0]
	start_num=int(start_cell[1])
	end_letter=end_cell[0]
	end_num=int(end_cell[1])	
	letter_diff=ord(start_letter)-ord(end_letter)
	num_dif=start_num-end_num
	if ord(start_cell[0])>ord('h') or int(start_cell[1])>8:
		return "Ошибка позиции!!!"
	elif ord(end_cell[0])>ord('h') or int(end_cell[1])>8:
		return "Ошибка позиции!!!"
	elif -1<=letter_diff<=1 and -1<=num_dif<=1:
		return "Да"
	else:
		return "Нет"

start=input("Введите стартовую позицию:").lower()
move=input("Введите следующую позицию:").lower()
end_move=king_move(start,move)
print(end_move)
# Немнога подкорректировал для себя, то бишь добавил проверку позиции.
# Введите стартовую позицию:a2
# Введите следующую позицию:b1
# Да
# Введите стартовую позицию:a1
# Введите следующую позицию:a3
# Нет