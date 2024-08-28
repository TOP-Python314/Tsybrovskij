def central_tendency(n1: float, n2: float, *numbers: float) -> dict[str, float]:
    numbs = [n1, n2] + list(numbers)
    numbs.sort()
    n = len(numbs)
    mult_numb = 1
    sums_harm = 0
    for numb in numbs:
        if numb != 0:
            mult_numb *= numb
            sums_harm += 1 / numb
    median_value = float(numbs[n // 2] if n % 2 == 1  else (numbs[n // 2 - 1] + numbs[n // 2]) / 2)
    arithmetic_value = sum(numbs) / n
    geometric_value = mult_numb ** (1 / n)
    harmonic_value = n / sums_harm
    actions = {
        'median': median_value,
        'arithmetic': arithmetic_value,
        'geometric': geometric_value,
        'harmonic': harmonic_value
    }
    return actions

# Примеры:
# >>> central_tendency(1, 2, 3, 4)
# {'median': 2.5, 'arithmetic': 2.5, 'geometric': 2.213363839400643, 'harmonic': 1.9200000000000004}
# >>>
# >>> sample = [1, 2, 3, 4, 5]
# >>> central_tendency(*sample)
# {'median': 3.0, 'arithmetic': 3.0, 'geometric': 2.605171084697352, 'harmonic': 2.18978102189781}