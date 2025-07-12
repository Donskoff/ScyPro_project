"""В этом модуле тестируются генераторы и функции.

И других конструкций.
"""

import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

from typing import List, Dict, Any, TypedDict, Optional


class Currency(TypedDict):
    """Класс."""

    name: str
    code: str


class OperationAmount(TypedDict):
    """Класс."""

    amount: str
    currency: Currency


class Transaction(TypedDict, total=False):
    """Класс."""

    id: int
    state: str
    date: str
    operationAmount: OperationAmount
    description: str
    from_account: Optional[str]  # Используем `from_account`, так как `from` является зарезервированным словом
    to: str


@pytest.mark.parametrize(
    "transactions, type_of_currency, expected_dict",
    [
        (
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                }
            ],
            "USD",
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                }
            ],
        )
    ],
)
def test_filter_by_currency(
    transactions: List[Dict[str, Any]], type_of_currency: str, expected_dict: List[Dict[str, Any]]
) -> None:
    """Функция тестирования с использованием параметризации."""
    result = list(filter_by_currency(transactions, type_of_currency))  # Преобразуем генератор в список
    assert result == expected_dict  # Сравниваем список результатов с ожидаемым выводом


def test_filter_by_currency_fik(transactions_data: List[Transaction]) -> None:
    # def test_filter_by_currency_fik(transactions_data):
    """Тестирование с фильтрацией по валюте "USD"."""
    result = list(filter_by_currency(transactions_data, "USD"))

    expected = [
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
            "id": 3,
            "state": "EXECUTED",
            "date": "2018-07-02T04:45:18.654321",
            "operationAmount": {"amount": "1500.00", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод на счет",
            "from": "Счет 34506830613657916952",
            "to": "Счет 45676614605963066702",
        },
    ]

    assert result == expected


def test_filter_by_currency_no_results(transactions_data):
    """Тестирование с фильтрацией по валюте "GBP" (нет таких транзакций)."""
    result = list(filter_by_currency(transactions_data, "GBP"))
    assert result == []


def test_transaction_descriptions(transactions_data_fix):
    """Тестирование генератора описаний транзакций."""
    descriptions = transaction_descriptions(transactions_data_fix)

    expected_descriptions = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]

    # Сравнение с использованием zip для обработки любой разницы в длине
    for expected, actual in zip(expected_descriptions, descriptions):
        assert expected == actual

    # Проверка, что не осталось больше значений в генераторе
    with pytest.raises(StopIteration):
        next(descriptions)  # Используем next() для провокации StopIteration


def test_card_number_generator(card_number_range):
    """Тестирование генератора номеров банковских карт."""
    start, end = card_number_range
    expected_numbers = [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",
    ]

    # Создаём генератор
    generated_numbers = list(card_number_generator(start, end))  # Преобразуем генератор в список

    assert generated_numbers == expected_numbers  # Сравниваем списки


@pytest.mark.parametrize(
    "start, end, expected_numbers",
    [
        (
            1,
            5,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ],
        ),
        (10, 12, ["0000 0000 0000 0010", "0000 0000 0000 0011", "0000 0000 0000 0012"]),
        (100, 102, ["0000 0000 0000 0100", "0000 0000 0000 0101", "0000 0000 0000 0102"]),
        (9995, 9998, ["0000 0000 0000 9995", "0000 0000 0000 9996", "0000 0000 0000 9997", "0000 0000 0000 9998"]),
    ],
)
def test_card_number_generator_par(start, end, expected_numbers):
    """Тестирование генератора номеров банковских карт с параметризацией."""
    # Генерируем номера карт
    generated_numbers = list(card_number_generator(start, end))  # Преобразуем генератор в список
    assert generated_numbers == expected_numbers  # Сравниваем списки


@pytest.mark.parametrize(
    "transactions, expected_descriptions",
    [
        (
            [
                {
                    "id": 1,
                    "state": "EXECUTED",
                    "date": "2023-01-01T00:00:00.000000",
                    "operationAmount": {"amount": "1000", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Тестовое описание 1",
                    "from": "Счет 1234567890123456",
                    "to": "Счет 6543210987654321",
                },
                {
                    "id": 2,
                    "state": "EXECUTED",
                    "date": "2023-01-02T00:00:00.000000",
                    "operationAmount": {"amount": "2000", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Тестовое описание 2",
                    "from": "Счет 1234567890123456",
                    "to": "Счет 6543210987654321",
                },
            ],
            ["Тестовое описание 1", "Тестовое описание 2"],
        ),
        (
            [
                {
                    "id": 3,
                    "state": "EXECUTED",
                    "date": "2023-01-03T00:00:00.000000",
                    "operationAmount": {"amount": "1500", "currency": {"name": "EUR", "code": "EUR"}},
                    "description": "Перевод между счетами",
                    "from": "Счет 1111111111111111",
                    "to": "Счет 2222222222222222",
                },
            ],
            ["Перевод между счетами"],
        ),
        ([], []),  # Пустой список  # Ожидаем пустой результат
    ],
)
def test_transaction_descriptions_par(transactions, expected_descriptions):
    """Тестирование генератора описаний транзакций с параметризацией."""
    descriptions = transaction_descriptions(transactions)

    # Преобразуем генератор в список
    generated_descriptions = list(descriptions)

    assert generated_descriptions == expected_descriptions
