import time
from functools import wraps
import logging


logging.basicConfig(filename='app.log', level=logging.INFO, encoding="utf-8")
logger = logging.getLogger()


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        logger.info(f"Функция {func.__name__} выполнена для списка из {len(args[0])} элементов за за {execution_time:.6f} секунд")
        return result

    return wrapper
