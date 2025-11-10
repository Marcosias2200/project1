import re


def validate_card_number(card_number: str) -> bool:
    """Проверяет, валиден ли номер карты (16 цифр)."""
    return bool(re.fullmatch(r"^\d{16}$", card_number))


def validate_account_number(account_number: str) -> bool:
    """Проверяет, валиден ли номер счета (20 цифр)."""
    return bool(re.fullmatch(r"^\d{20}$", account_number))


def get_mask_card_number(card_number: str) -> str:
    """Возвращает замаскированный номер банковской карты."""
    return f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Возвращает замаскированный номер банковского счета."""
    return "**" + account_number[-4:]


