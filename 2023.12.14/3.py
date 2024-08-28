def numbers_strip(numbers: list, n: int = 1, copy : bool = False) -> list:
    if copy:
        numbers = numbers.copy()
    elif n * 2 >= len(numbers):
        raise ValueError('Максимальное и минимальное число для удаления не может быть больше половины количества элементов в списке!')
    for _ in range(n):
        numbers.remove(min(numbers))
        numbers.remove(max(numbers))
    return numbers
 
# Примеры: 
# >>> sample = [1, 2, 3, 4]
# >>> sample_stripped = numbers_strip(sample)
# >>> sample_stripped
# [2, 3]
# >>> sample is sample_stripped
# True
# >>>
# >>> sample = [10, 20, 30, 40, 50]
# >>> sample_stripped = numbers_strip(sample, 2, copy=True)
# >>> sample_stripped
# [30]
# >>> sample is sample_stripped
# False