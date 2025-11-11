import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize("state,expected", [
    ('EXECUTED', [
        {'id': 1, 'amount': 100, 'state': 'EXECUTED'},
        {'id': 3, 'amount': 150, 'state': 'EXECUTED'},
        {'id': 5, 'amount': 50, 'state': 'EXECUTED'},
    ]),
    ('CANCELED', [{'id': 2, 'amount': 250, 'state': 'CANCELED'}]),
    ('PENDING', [{'id': 4, 'amount': 300, 'state': 'PENDING'}]),
    ('FAILED', []),
])


def test_filter_by_state(transactions, state, expected):
    """Тестирует фильтрацию транзакций по состоянию."""
    result = filter_by_state(transactions, state)
    assert result == expected


def test_filter_by_state_empty():
    """Тестирует фильтрацию для пустого списка транзакций."""
    assert filter_by_state([], 'EXECUTED') == []




@pytest.mark.parametrize("descending,expected", [
    (True, [
        {'id': 5, 'amount': 50, 'date': '2023-09-03T15:00:00.000000'},
        {'id': 2, 'amount': 250, 'date': '2023-09-03T12:00:00.000000'},
        {'id': 3, 'amount': 150, 'date': '2023-09-02T14:00:00.000000'},
        {'id': 1, 'amount': 100, 'date': '2023-09-01T10:00:00.000000'},
        {'id': 4, 'amount': 300, 'date': '2023-09-01T09:00:00.000000'},
    ]),
    (False, [
        {'id': 4, 'amount': 300, 'date': '2023-09-01T09:00:00.000000'},
        {'id': 1, 'amount': 100, 'date': '2023-09-01T10:00:00.000000'},
        {'id': 3, 'amount': 150, 'date': '2023-09-02T14:00:00.000000'},
        {'id': 2, 'amount': 250, 'date': '2023-09-03T12:00:00.000000'},
        {'id': 5, 'amount': 50, 'date': '2023-09-03T15:00:00.000000'},
    ]),
])


def test_sort_by_date(sort_bate, descending, expected):
    """Тестирует сортировку транзакций по дате."""
    result = sort_by_date(sort_bate, descending)
    assert result == expected


def test_sort_by_date_empty():
    """Тестирует сортировку для пустого списка транзакций."""
    assert sort_by_date([]) == []


def test_sort_by_date_invalid_data():
    """Тестирует обработку ошибки при неправильном формате даты."""
    with pytest.raises(KeyError):
        sort_by_date([{'id': 1, 'amount': 100}])  # Нет ключа 'date'