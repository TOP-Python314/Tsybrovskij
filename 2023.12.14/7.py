def int_base(number: str, source_system: int, target_system: int) -> str or None:
    number_systems = {chr(key): value for key, value in zip(range(97,123), range(10,36))}
    number_systems.update({str(i): i for i in range(10)})
    if not (2 <= target_system <= 36 and 2 <= source_system <= 36):
        return None
    number = number.lower()
    for char in number:
        if char not in number_systems or number_systems[char] >= source_system:
            return None
    result = int(number, source_system)
    res = trans_numb_sys(result, target_system)
    return res
        # выполнение перевода в другую систему счисления:
def trans_numb_sys(n, b):
    res = []
    result = ''
    number_systems = {chr(key): value for key, value in zip(range(97,123), range(10,36))}
    while n != 0:
        res.append(n % b)
        n //= b
    res.reverse()
    for symb in res:
        if symb >= 10:
            for key, value in number_systems.items():
                if value == symb:
                    result += key
                    break
        else:
            result += str(symb)
    return result

# Промер:
# >>> print(int_base('ff00', 16, 2))
# 1111111100000000
# >>> print(int_base('1101010', 2, 30))
# 3g