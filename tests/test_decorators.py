import pytest
from src.decorators  import log

@log()
def add(a, b):
    return a + b

@log()
def divide(a, b):
    return a / b

@log()
def raise_exception():
    raise ValueError("Это тестовое исключение.")

