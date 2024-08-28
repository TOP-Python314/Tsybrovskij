def orth_triangle(*,cathetus1: float = None, cathetus2: float = None, hypotenuse: float = None) -> None or float:
    if hypotenuse is None and None not in (cathetus1, cathetus2):
        return (cathetus1 ** 2 + cathetus2 ** 2) ** (1 / 2)
    elif cathetus2 is None and None not in (cathetus1, hypotenuse) and hypotenuse > cathetus1:
        return (hypotenuse ** 2 - cathetus1 ** 2) ** (1 / 2)
    elif cathetus1 is None and None not in (cathetus2, hypotenuse) and hypotenuse > cathetus2:
        return (hypotenuse ** 2 - cathetus2 ** 2) ** (1 / 2)
    else:
        return None
# Примеры:
# >>> orth_triangle(cathetus1=3, hypotenuse=5)
# 4.0
# >>> orth_triangle(cathetus1=8, cathetus2=15)
# 17.0
# >>> print(orth_triangle(cathetus2=9, hypotenuse=3))
# None