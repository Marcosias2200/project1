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

def test_add(caplog):
    with caplog.at_level('INFO'):
        result = add(2, 3)
    # Проверяем, что результат корректен
    assert result == 5
    # Проверяем логи
    assert "add ok" in caplog.text

def test_divide(caplog):
    with caplog.at_level('INFO'):
        result = divide(10, 2)
    # Проверяем, что результат корректен
    assert result == 5.0
    # Проверяем логи
    assert "divide ok" in caplog.text

def test_divide_zero(caplog):
    with caplog.at_level('ERROR'):
        with pytest.raises(ZeroDivisionError):
            divide(10, 0)
    # Проверяем, что запись ошибке присутствует в логах
    assert "divide error: ZeroDivisionError. Inputs: (10, 0), {}" in caplog.text

def test_raise_exception(caplog):
    with caplog.at_level('ERROR'):
        with pytest.raises(ValueError):
            raise_exception()
    # Проверяем, что запись ошибке присутствует в логах
    assert "raise_exception error: ValueError. Inputs: (), {}" in caplog.text