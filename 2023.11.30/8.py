def fibonacci_numbers(length):
    numbers = [1]
    while len(numbers) < length:
        if len(numbers) == 1:
            next_number = 1
        else:
            next_number = numbers[-1] + numbers[-2]
        numbers.append(next_number)
    return numbers
number = int(input('Введите количество цифр в последовательности Фибоначчи: '))
result = fibonacci_numbers(number)
print(' '.join(map(str, result)))

# Введите количество цифр в последовательности Фибоначчи: 1
# 1
# Введите количество цифр в последовательности Фибоначчи: 17
# 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597