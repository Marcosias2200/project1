import functools
import logging

def log(filename=None):
    """
    Декоратор для логирования начала и конца выполнения функции,
    а также её результата или возникших ошибок.
    """
    # Настройка логирования
    if filename:
        logging.basicConfig(filename=filename, level=logging.INFO,
                            format='%(message)s')  # Убрали дату и уровень
    else:
        logging.basicConfig(level=logging.INFO,
                            format='%(message)s')  # Убрали дату и уровень

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                logging.info(f"{func.__name__} ok")  # Успешное выполнение
                return result
            except Exception as e:
                logging.error(f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}")  # Ошибка выполнения
                raise
        return wrapper
    return decorator