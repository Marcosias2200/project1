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