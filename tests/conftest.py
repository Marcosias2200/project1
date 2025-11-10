import pytest

@pytest.fixture
def valid_card():
    return "1234567812345678"


@pytest.fixture
def mask_number():
    return "7000 79** **** 6361"


@pytest.fixture
def get_mask():
    return "**4305"


@pytest.fixture
def transactions():
    return [
        {'id': 1, 'amount': 100, 'state': 'EXECUTED'},
        {'id': 2, 'amount': 250, 'state': 'CANCELED'},
        {'id': 3, 'amount': 150, 'state': 'EXECUTED'},
        {'id': 4, 'amount': 300, 'state': 'PENDING'},
        {'id': 5, 'amount': 50, 'state': 'EXECUTED'},
    ]


@pytest.fixture
def sort_bate():
    return [
        {'id': 1, 'amount': 100, 'date': '2023-09-01T10:00:00.000000'},
        {'id': 2, 'amount': 250, 'date': '2023-09-03T12:00:00.000000'},
        {'id': 3, 'amount': 150, 'date': '2023-09-02T14:00:00.000000'},
        {'id': 4, 'amount': 300, 'date': '2023-09-01T09:00:00.000000'},
        {'id': 5, 'amount': 50, 'date': '2023-09-03T15:00:00.000000'},
    ]