"""Здесь расположены фикстуры для тестирования функций проекта."""

import json
from typing import Any, Dict, List
from unittest import mock

import pytest


@pytest.fixture
def mask_card_number() -> str:
    """Фикстура."""
    return "1234 1234 1234 1234"


@pytest.fixture
def mask_card_number_out() -> str:
    """Фикстура."""
    return "Введён некорректный номер карты"


@pytest.fixture
def mask_account() -> str:
    """Фикстура."""
    return "12345678909876543212"


@pytest.fixture
def mask_account_out() -> str:
    """Фикстура."""
    return "Некорректный номер счёта"


@pytest.fixture
def account_card_check() -> str:
    """Фикстура."""
    return "Счёт **4305"


@pytest.fixture
def account_card_number() -> str:
    """Фикстура."""
    return "Visa Platinum 7000 79** **** 6361"


@pytest.fixture
def get_date_par() -> str:
    """Фикстура."""
    return "11.03.2024"


@pytest.fixture
def filter_by_state_func() -> List[Dict[str, Any]]:
    """Фикстура."""
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def sort_by_date_func() -> List[Dict[str, Any]]:
    """Фикстура."""
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def transactions_data() -> List[Dict[str, Any]]:
    """Фиктура для генерации тестовых данных транзакций."""
    return [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 2,
            "state": "EXECUTED",
            "date": "2018-07-01T03:15:30.123456",
            "operationAmount": {"amount": "5000.00", "currency": {"name": "EUR", "code": "EUR"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 05106830613657916952",
            "to": "Счет 26776614605963066702",
        },
        {
            "id": 3,
            "state": "EXECUTED",
            "date": "2018-07-02T04:45:18.654321",
            "operationAmount": {"amount": "1500.00", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод на счет",
            "from": "Счет 34506830613657916952",
            "to": "Счет 45676614605963066702",
        },
    ]


@pytest.fixture
def transactions_data_fix() -> List[Dict[str, Any]]:
    """Фиктура, возвращающая список тестовых транзакций."""
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


@pytest.fixture
def card_number_range() -> tuple:
    """Фиктура для генерации диапазона номеров карт."""
    return (1, 5)  # Вы можете изменить диапазон по необходимости


@pytest.fixture
def calculate_usd_to_rub_fix() -> float:
    """Фиктура для генерации диапазона номеров карт."""
    return 0.5


@pytest.fixture
def mock_file_not_found(mocker: mock.MagicMock) -> None:
    """Фикстура для случая, когда файл не существует."""
    mocker.patch("os.path.isfile", return_value=False)


@pytest.fixture
def mock_empty_file(mocker: mock.MagicMock) -> None:
    """Фикстура для пустого файла."""
    mock_open = mock.mock_open(read_data="")
    mocker.patch("builtins.open", mock_open)


@pytest.fixture
def mock_invalid_json(mocker: mock.MagicMock) -> None:
    """Фикстура для файла с некорректным JSON."""
    mock_open = mock.mock_open(read_data=json.dumps({"id": 1, "amount": 100}))  # Это не список
    mocker.patch("builtins.open", mock_open)


@pytest.fixture
def mock_valid_json(mocker: mock.MagicMock) -> None:
    """Фикстура для файла с корректным JSON."""
    test_data = [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]
    mock_open = mock.mock_open(read_data=json.dumps(test_data))
    mocker.patch("builtins.open", mock_open)
