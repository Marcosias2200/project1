import pytest

from src.widget import mask_account_card, get_date


@pytest.mark.parametrize("card_account, expected", [
    ("Карта 3231122332314432", "Карта 3231 12** **** 4432"),
    ("Карта 4531451133332219", "Карта 4531 45** **** 2219"),
    ("Счет 123456789012345678", "Счет **5678"),
    ("Счет 8765432101234567", "Счет **4567"),
    ("Счет 4444333322221111", "Счет **1111")
    ])
def test_mask_account_card(card_account, expected):
    assert mask_account_card(card_account) == expected


@pytest.mark.parametrize("date, expected", [
    ("2023.03.15", "15.03.2023"),
    ("2021.12.01", "01.12.2021"),
    ("2000.01.31", "31.01.2000"),
    ("2022.04.05", "05.04.2022"),
    ("1999.09.09", "09.09.1999")
])
def test_get_date(date, expected):
    assert get_date(date) == expected