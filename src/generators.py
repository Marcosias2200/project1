from typing import List, Dict, Generator


def filter_by_currency(transactions: List[Dict[str, str]], currency: str) -> Generator[Dict[str, str], None, None]:
    """Генератор для фильтрации транзакций по валюте"""
    for transaction in transactions:
        if transaction.get("currency") == currency:
            yield transaction


def transaction_descriptions(transactions: List[Dict[str, str]]) -> Generator[str, None, None]:
    """Генератор для получения описаний транзакций."""
    for transaction in transactions:
        description = f"Transaction ID: {transaction['id']}, Amount: {transaction['amount']:.2f} {transaction['currency']}, Date: {transaction['date']}"
        yield description


def card_number_generator(start: int, end: int) -> Generator[str, None, None]:
    """Генератор для создания номеров банковских карт в указанном диапазоне."""
    for number in range(start, end + 1):
        yield f"{number:016}"[:4] + " " + f"{number:016}"[4:8] + " " + f"{number:016}"[8:12] + " " + f"{number:016}"[
                                                                                                     12:16]