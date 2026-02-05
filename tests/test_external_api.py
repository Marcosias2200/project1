import pytest
from unittest.mock import patch
from external_api import convert_to_rubles

@pytest.fixture
def mock_transaction():
    return {"amount": 100.0, "currency": "USD"}

@patch('external_api.requests.get')
@patch('os.getenv')
def test_convert_to_rubles_usd(mock_get, mock_getenv, mock_transaction):
    mock_getenv.return_value = 'dummy_token'
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {'result': 7500}

    # Поскольку 100 USD = 7500 RUB по нашему мокированному ответу
    result = convert_to_rubles(mock_transaction)
    assert result == 7500

@patch('external_api.requests.get')
@patch('os.getenv')
def test_convert_to_rubles_rub(mock_get, mock_getenv, mock_transaction):
    mock_transaction['currency'] = 'RUB'
    result = convert_to_rubles(mock_transaction)
    assert result == 100.0  # Сумма должна оставаться неизменной для RUB

@patch('external_api.requests.get')
@patch('os.getenv')
def test_convert_to_rubles_unsupported_currency(mock_get, mock_getenv, mock_transaction):
    mock_transaction['currency'] = 'JPY'
    result = convert_to_rubles(mock_transaction)
    assert result == 100.0  # Вернуть исходную сумму при неподдерживаемой валюте