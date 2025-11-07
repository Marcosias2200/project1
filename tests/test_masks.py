import pytest

from src.masks import validate_card_number, get_mask_account, get_mask_card_number


def test_valid_card(valid_card):
    assert validate_card_number(valid_card) is True


@pytest.mark.parametrize("card_numbers", [
    "123456781234567",   # Меньше 16 цифр
    "12345678123456789", # Больше 16 цифр
    "123456781234567a",  # Содержит буквы
    "1234-5678-1234-5678", # Формат не соответствует
    "",                   # Пустая строка
    ])
def test_invalid_cards(card_numbers):
   assert validate_card_number(card_numbers) is False


def test_get_mask_card_number(mask_number):
    assert get_mask_card_number("7000798143256361") == mask_number

