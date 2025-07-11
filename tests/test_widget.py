"""Этот модуль содержит тестовые функции."""

import pytest

from src.widget import get_date, mask_account_card


def test_mask_account_card_check(account_card_check):
    """Функция тестирования с использованием фикстур."""
    assert mask_account_card("Счёт 73654108430135874305") == account_card_check


def test_mask_account_card_number(account_card_number):
    """Функция тестирования с использованием фикстур."""
    assert mask_account_card("Visa Platinum 7000792289606361") == account_card_number


@pytest.mark.parametrize(
    "card_number_check, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Visa Platinum 7000 7922 8960 6361", "Введённые вами данные не корректны!"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Счет 73654108XXfXX", "Введённые вами данные не корректны!"),
        ("", "Введите корректные данные!"),
        ("Счет 736541084301358743052", "Введённые вами данные не корректны!"),
        ("Visa Platinum 7000", "Введённые вами данные не корректны!"),
    ],
)
def test_get_mask_card_number(card_number_check, expected):
    """Функция тестирования с использованием параметризации."""
    assert mask_account_card(card_number_check) == expected


def test_get_date(get_date_par):
    """Функция тестирования с использованием фикстур."""
    assert get_date("2024-03-11T02:26:18.671407") == get_date_par


@pytest.mark.parametrize(
    "date_par, expected_date",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2024-03-11 02:26:18.671407", "Неверный ввод даты!"),
        ("YYYY-03-11T02:26:18.671407", "Дата не соответствует формату ISO 8601!"),
        ("", "Введите правильно дату, нет данных!"),
        ("1111-11-11T111111111111111", "Неверный ввод даты!"),
        ("2024-13-11T02:26:18.671407", "Дата не соответствует формату ISO 8601!"),
        ("2024-11-33T02:26:18.671407", "Дата не соответствует формату ISO 8601!"),
    ],
)
def test_get_date_par(date_par, expected_date):
    """Функция тестирования с использованием параметризации."""
    assert get_date(date_par) == expected_date
