import pytest

@pytest.fixture
def mask_card_number():
    return '1234 1234 1234 1234'


@pytest.fixture
def mask_card_number_out():
    return 'Введён некорректный номер карты'


@pytest.fixture
def mask_account():
    return '12345678909876543212'


@pytest.fixture
def mask_account_out():
    return 'Некорректный номер счёта'