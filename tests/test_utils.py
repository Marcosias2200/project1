import pytest
import json
import os
from utils.utils import load_transactions_from_json

@pytest.fixture
def json_file(tmp_path):
    """Фикстура для создания временного JSON-файла с транзакциями."""
    data = [
        {"id": 1, "amount": 100.0, "currency": "USD"},
        {"id": 2, "amount": 200.0, "currency": "EUR"},
    ]
    file_path = tmp_path / "operations.json"
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f)
    return str(file_path)

def test_load_transactions_from_jsons(json_file):
    transaction = load_transactions_from_json(json_file)
    assert len(transaction) == 2

def test_load_transactions_empty_file(tmp_path):
    file_patch = tmp_path / "empty.json"
    with open(file_patch, 'w'):  # Создаем пустой файл
        pass
    transaction = load_transactions_from_json(file_patch)
    assert transaction == []

def test_load_transactions_file_not_found():
    transaction = load_transactions_from_json('non_existent_file.json')
    assert transaction == []