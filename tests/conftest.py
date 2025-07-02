"""Здесь расположены фикстуры для тестирования функций проекта."""

import pytest


@pytest.fixture
def mask_card_number():
    """Фикстура."""
    return "1234 1234 1234 1234"


@pytest.fixture
def mask_card_number_out():
    """Фикстура."""
    return "Введён некорректный номер карты"


@pytest.fixture
def mask_account():
    """Фикстура."""
    return "12345678909876543212"


@pytest.fixture
def mask_account_out():
    """Фикстура."""
    return "Некорректный номер счёта"


@pytest.fixture
def account_card_check():
    """Фикстура."""
    return "Счёт **4305"


@pytest.fixture
def account_card_number():
    """Фикстура."""
    return "Visa Platinum 7000 79** **** 6361"


@pytest.fixture
def get_date_par():
    """Фикстура."""
    return "11.03.2024"


@pytest.fixture
def filter_by_state_func():
    """Фикстура."""
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def sort_by_date_func():
    """Фикстура."""
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
