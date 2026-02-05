import json
import os
from typing import List, Dict, Any


def load_transactions_from_json(file_path: str) -> List[Dict[str, Any]]:
    """
    Загружает данные о финансовых транзакциях из JSON-файла.

    :param file_path: Путь до JSON-файла.
    :return: Список словарей с данными о транзакциях или пустой список в случае ошибки.
    """
    if not os.path.exists(file_path):
        return []

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            else:
                return []
    except (json.JSONDecodeError, FileNotFoundError):
        return []