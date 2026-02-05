import os
import requests
from utils import load_dotenv
from typing import Dict

load_dotenv()  # Загружает переменные окружения из файла .env

API_URL = "https://api.apilayer.com/exchangerates_data/convert"


def convert_to_rubles(transaction: Dict[str, Any]) -> float:
    """
    Конвертирует сумму транзакции в рубли.

    :param transaction: Словарь с данными о транзакции.
    :return: Сумма транзакции в рублях.
    """
    amount = transaction['amount']
    currency = transaction['currency']

    if currency == 'RUB':
        return amount

    # Получаем токен из переменных окружения
    token = os.getenv('API_TOKEN')

    if currency in ['USD', 'EUR']:
        response = requests.get(API_URL, params={
            'from': currency,
            'to': 'RUB',
            'amount': amount,
            'apikey': token
        })

        if response.status_code == 200:
            data = response.json()
            return data['result']

    return amount  # Если валюта не поддерживается, возвращаем исходную сумму