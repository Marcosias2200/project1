import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator



# Пример данных для тестов
@pytest.fixture
def transactions():
    """Фикстура для создания списка транзакций."""
    return [
        {"id": 1, "amount": 100.0, "currency": "USD", "date": "2023-01-01"},
        {"id": 2, "amount": 200.0, "currency": "EUR", "date": "2023-01-01"},
        {"id": 3, "amount": 150.0, "currency": "USD", "date": "2023-01-02"},
        {"id": 4, "amount": 300.0, "currency": "JPY", "date": "2023-01-02"},
    ]

@pytest.mark.parametrize("currency, expected_ids", [
    ("USD", [1, 3]),
    ("EUR", [2]),
    ("JPY", [4]),
    ("GBP", []),  # Валюта, которой нет в списке
])
def test_filter_by_currency(transactions, currency, expected_ids):
    """Тестируем фильтрацию по валюте."""
    usd_transactions = list(filter_by_currency(transactions, currency))
    actual_ids = [transaction["id"] for transaction in usd_transactions]
    assert actual_ids == expected_ids

def test_transaction_descriptions(transactions):
    """Тестируем генерацию описаний транзакций."""
    descriptions = list(transaction_descriptions(transactions))
    expected_descriptions = [
        "Transaction ID: 1, Amount: 100.00 USD, Date: 2023-01-01",
        "Transaction ID: 2, Amount: 200.00 EUR, Date: 2023-01-01",
        "Transaction ID: 3, Amount: 150.00 USD, Date: 2023-01-02",
        "Transaction ID: 4, Amount: 300.00 JPY, Date: 2023-01-02",
    ]
    assert descriptions == expected_descriptions

@pytest.mark.parametrize("start, end, expected_numbers", [
    (1, 5, [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005"]),
    (9999, 10002, [
        "0000 0000 0000 9999",
        "0000 0000 0001 0000",
        "0000 0000 0001 0001",
        "0000 0000 0001 0002"]),
])
def test_card_number_generator(start, end, expected_numbers):
    """Тестируем генерацию номеров карт."""
    generated_numbers = list(card_number_generator(start, end))
    assert generated_numbers == expected_numbers
