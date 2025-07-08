"""Декоратор.

Автоматически логировать начало и конец выполнения функции,
а также ее результаты или возникшие ошибки.
"""

import functools
import logging
import sys


def setup_logging(filename=None):
    """Настройка логирования."""
    if filename:
        logging.basicConfig(filename=filename, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def log(filename=None):
    """Декоратор для автоматического логирования начала и конца выполнения функции."""
    setup_logging(filename)

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):

            try:
                result = func(*args, **kwargs)
                logging.info(f"Starting {func.__name__} with args: {args}, kwargs: {kwargs}")
                logging.info(f"{func.__name__} ok. Result: {result}")
                print(f'Function {func.__name__} called whith {args} and kwargs {kwargs}. Result: {result}')
                return result
            except Exception as e:
                logging.error(f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}")
                raise

        return wrapper

    return decorator


# Пример использования декоратора
# @log(filename="src/mylog.txt")
@log(filename="")
def my_function(x, y):
    """Функция."""
    return x + y

my_function(12, 78)
