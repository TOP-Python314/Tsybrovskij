def logger(func):
    def wrapper(*args, **kwargs):
        arg_names = func.__code__.co_varnames[:func.__code__.co_argcount]
        default_values = func.__defaults__ or {}
        kw_default_values = func.__kwdefaults__ or {}
        arg_values = list(args)
        for i, name in enumerate(arg_names):
            if i >= len(arg_values):
                if name in kw_default_values:
                    arg_values.append(kw_default_values[name])
                elif len(default_values) > i - len(kw_default_values):
                    arg_values.append(default_values[i - len(kw_default_values)])
        arg_string = ', '.join(repr(arg) for arg in arg_values)
        kwarg_string = ', '.join(f"{key}={value!r}" for key, value in kwargs.items())
        if kwarg_string:
            arg_string += ', ' + kwarg_string
        try:
            result = func(*args, **kwargs)
            print(f"{func.__name__}({arg_string}) -> {result!r}")
            return result
        except Exception as e:
            print(f"{func.__name__}({arg_string}) .. {type(e).__name__}: {e}")
            pass
    return wrapper
    
# >>> def div_round(num1, num2, *, digits=0):
# ...     return round(num1 / num2, digits)
# ...
# >>> div_round = logger(div_round)
# >>> div_round(1, 3, digits=2)
# div_round(1, 3, digits=2) -> 0.33
# 0.33
# >>> div_round(7, 2)
# div_round(7, 2) -> 4.0
# 4.0
# >>> div_round(5, 0)
# div_round(5, 0) .. ZeroDivisionError: division by zero