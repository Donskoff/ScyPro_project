"""Этот модуль содержит тестовые функции."""

import pytest

from src.masks import get_mask_card_number, get_mask_account


def test_mask_card_number(mask_card_number):
    """Функция тестирования с использованием фикстур."""
    assert get_mask_card_number(mask_card_number) == "1234 12** **** 1234"


def test_get_mask_card_out(mask_card_number_out):
    """Функция тестирования с использованием фикстур."""
    assert get_mask_card_number("1234 1234 1234") == mask_card_number_out


@pytest.mark.parametrize(
    "card_number, expected1",
    [
        ("qwertrewqwertyui", "Введён некорректный номер карты"),
        ("1234 1234 1234", "Введён некорректный номер карты"),
        ("123N 1234 1234", "Введён некорректный номер карты"),
        ('', "Введён некорректный номер карты"),
        ("qwer qwer qwer qwer", "Введён некорректный номер карты"),
        ("123412341234", "Введён некорректный номер карты"),
        ("1234012340123401234", "Введён некорректный номер карты"),
    ],
)
def test_get_mask_card_number(card_number, expected1):
    """Функция тестирования с использованием параметризации."""
    assert get_mask_card_number(card_number) == expected1


def test_mask_account(mask_account):
    """Функция тестирования с использованием фикстур."""
    assert get_mask_account(mask_account) == "**3212"


def test_get_mask_account_out(mask_account_out):
    """Функция тестирования с использованием фикстур."""
    assert get_mask_account("1234567890987654321211111") == mask_account_out


@pytest.mark.parametrize(
    "account, expected",
    [
        ("123456789098765", "Некорректный номер счёта"),
        ("7000 7922 8960 6361", "Некорректный номер счёта"),
        ("", "Некорректный номер счёта"),
        ("123456789101112131415161718192021", "Некорректный номер счёта"),
        ("1234qwertyuiop", "Некорректный номер счёта"),
        ("", "Некорректный номер счёта"),
        ("qwerwwwweeeerrrr", "Некорректный номер счёта"),
        ("                 ", "Некорректный номер счёта"),
        ("", "Некорректный номер счёта"),
    ],
)
def test_get_mask_account(account, expected):
    """Функция тестирования с использованием параметризации."""
    assert get_mask_account(account) == expected
