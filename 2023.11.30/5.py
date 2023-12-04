telegram = input('Введите текст телеграммы: ')
price = 30
amount = len(telegram.replace(" ", ""))
check = amount * price	
print(f'{check//100} руб. {check%100} коп.')

# Введите текст телеграммы: грузите апельсины бочках братья карамазовы
# 11 руб. 40 коп.