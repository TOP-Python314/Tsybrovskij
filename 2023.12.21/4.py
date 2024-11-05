def repeat(times=2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator
    
# >>> def testing_function():
# ...     print('python')
# ...
# >>> testing_function = repeat(4)(testing_function)
# >>> testing_function()
# python
# python
# python
# python