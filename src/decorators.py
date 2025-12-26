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
                            format='%(asctime)s - %(levelname)s - %(message)s')
    else:
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                logging.info(f"Начало выполнения функции: {func.__name__} с аргументами {args}, {kwargs}")
                result = func(*args, **kwargs)
                logging.info(f"Функция: {func.__name__} завершена успешно, результат: {result}")
                return result
            except Exception as e:
                logging.error(f"Ошибка при выполнении функции: {func.__name__}, тип ошибки: {type(e).__name__}, аргументы: {args}, {kwargs}")
                raise
        return wrapper
    return decorator