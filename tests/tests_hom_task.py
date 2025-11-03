import pytest

from src.masks import validate_card_number


def test_masks():
    assert validate_card_number


def valid_card_number():
    return "1234567812345678"

@pytest.fixture
def invalid_card_numbers():
        return [

                "123456781234567",  # Меньше 16 цифр
                "12345678123456789",  # Больше 16 цифр
                "123456781234567a",  # Содержит буквы
                "1234-5678-1234-5678",  # Формат не соответствует
                "",  # Пустая строка

        ]
def test_validate_card_number_with_valid_input(valid_card_numbers):
    assert validate_card_number(valid_card_numbers) is True

def test_validate_card_number_with_invalid_input(invalid_card_numbers):
    for card_number in invalid_card_numbers:
        assert validate_card_number(card_number) is False

