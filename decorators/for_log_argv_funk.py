def log_arguments(func):
    def wrapper(*args, **kwargs):
        print(f'Arguments for {func.__name__}: {args}, {kwargs}')
        result = func(*args, **kwargs)
        print(f'Result of {func.__name__}: {result}')
        return result
    return wrapper
