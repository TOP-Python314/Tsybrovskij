def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def simpl_numbers(numbers):
    start = 10**(numbers - 1) 
    end = 10**numbers  
    count = 0  
    for num in range(start, end):
        if is_prime(num):
            count += 1 
    return count 

n = int(input("Введите количество разрядов: "))
result = simpl_numbers(n)
print(result)

# Введите количество разрядов: 3
# 143