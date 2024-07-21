def function_start(func):
    def wrapper(*args, **kwargs):
        print(f'Function {func.__name__} has been started')
        result = func(*args, **kwargs)
        print(f'Function {func.__name__} has been finished')
        return result
    return wrapper
