def taxi_cost(long_route,wait_time = 0) -> int | None:
    start_cost = 80
    cost_route = int(long_route / 150 * 6)
    cost_wait = int(wait_time * 3)
    if long_route >= 0 and wait_time >= 0:
        if long_route == 0:
            finile_cost = start_cost * 2 + cost_route + cost_wait
        else:
            finile_cost = start_cost + cost_route + cost_wait
        return finile_cost
    else:
        return None

# Пример:
# >>> taxi_cost(1500)
# 140
# >>> taxi_cost(2560)
# 182
# >>> taxi_cost(0,5)
# 175
# >>> taxi_cost(42130,8)
# 1789
# >>> print(taxi_cost(-300))
# None