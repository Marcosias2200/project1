import pytest


from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

# Пример данных для тестов
transactions = [
    {"id": 1, "amount": 100.0, "currency": "USD", "date": "2023-01-01"},
    {"id": 2, "amount": 200.0, "currency": "EUR", "date": "2023-01-01"},
    {"id": 3, "amount": 150.0, "currency": "USD", "date": "2023-01-02"},
    {"id": 4, "amount": 300.0, "currency": "JPY", "date": "2023-01-02"},
]


def test_filter_by_currency():
    # Тестируем фильтрацию по валюте
    usd_transactions = list(filter_by_currency(transactions, "USD"))
    assert len(usd_transactions) == 2
    assert usd_transactions[0]["id"] == 1
    assert usd_transactions[1]["id"] == 3

    eur_transactions = list(filter_by_currency(transactions, "EUR"))
    assert len(eur_transactions) == 1
    assert eur_transactions[0]["id"] == 2

    jpy_transactions = list(filter_by_currency(transactions, "JPY"))
    assert len(jpy_transactions) == 1
    assert jpy_transactions[0]["id"] == 4


def test_transaction_descriptions():
    # Тестируем генерацию описаний транзакций
    descriptions = list(transaction_descriptions(transactions))
    assert len(descriptions) == 4
    assert descriptions[0] == "Transaction ID: 1, Amount: 100.00 USD, Date: 2023-01-01"
    assert descriptions[1] == "Transaction ID: 2, Amount: 200.00 EUR, Date: 2023-01-01"
    assert descriptions[2] == "Transaction ID: 3, Amount: 150.00 USD, Date: 2023-01-02"
    assert descriptions[3] == "Transaction ID: 4, Amount: 300.00 JPY, Date: 2023-01-02"


def test_card_number_generator():
    # Тестируем генератор номеров карт
    generated_numbers = list(card_number_generator(1, 5))
    expected_numbers = [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005"
    ]

    assert generated_numbers == expected_numbers

    # Проверяем, что генерация работает правильно в большом диапазоне
    large_generated_numbers = list(card_number_generator(9999, 10002))
    assert len(large_generated_numbers) == 4
    assert large_generated_numbers[0] == "0000 0000 9999 9999"
    assert large_generated_numbers[1] == "0000 0001 0000 0000"
    assert large_generated_numbers[2] == "0000 0001 0000 0001"
    assert large_generated_numbers[3] == "0000 0001 0000 0002"
