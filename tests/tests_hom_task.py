import pytest

from src.masks import validate_card_number


@pytest.fixture
def valid_card():
    return "1234567812345678"

# Фикстура для списка невалидных номеров карт
@pytest.fixture(params=[
    "123456781234567",   # Меньше 16 цифр
    "12345678123456789", # Больше 16 цифр
    "123456781234567a",  # Содержит буквы
    "1234-5678-1234-5678", # Формат не соответствует
    "",                   # Пустая строка
])
def invalid_card(request):
    return request.param

def test_valid_card(valid_card):
    assert validate_card_number(valid_card) is True

def test_invalid_cards(invalid_card):
    assert validate_card_number(invalid_card) is False

