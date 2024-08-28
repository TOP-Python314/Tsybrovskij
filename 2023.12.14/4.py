def countable_nouns(n: int, tuple_list: tuple[str, str, str]) -> str:
    num_series1 = {0}|{x for x in range(5,21)}
    num_series2 = {x for x in range(2,5)}
    # Если n - третий ряд то выводить tuple_list[2]
    if n % 100 in num_series1 or n % 10 == 0:
        return tuple_list[2]
    elif n % 10 in num_series2:
        return tuple_list[1]
    else:
        return tuple_list[0]

# Примеры:
# >>> countable_nouns(1, ("год", "года", "лет"))
# 'год'
# >>> countable_nouns(2, ("год", "года", "лет"))
# 'года'
# >>> countable_nouns(10, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(12, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(22, ("год", "года", "лет"))
# 'года'