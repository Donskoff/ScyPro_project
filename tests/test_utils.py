"""Тест.

Модуля utils.py/
"""

from src.utils import load_transactions, convert_transaction_to_rub
import json
from unittest.mock import mock_open, patch
import pytest


def test_convert_transaction_to_rub_success_eur():
    """Тестируем конвертацию из EUR в RUB."""
    transaction = {"operationAmount": {"amount": "100", "currency": {"code": "EUR", "name": "EUR"}}}
    # Предположим, что value_rub = 80.0
    with patch("src.external_api.value_rub", new=80.0):
        modified_transaction = convert_transaction_to_rub(transaction)

    assert modified_transaction["operationAmount"]["amount"] == 8665.0432
    assert modified_transaction["operationAmount"]["currency"]["code"] == "RUB"


def test_convert_transaction_to_rub_invalid_currency():
    """Тестируем случай с неизвестной валютой."""
    transaction = {"operationAmount": {"amount": "100", "currency": {"code": "GBP", "name": "GBP"}}}

    with pytest.raises(ValueError, match="Неизвестная валюта: GBP"):
        convert_transaction_to_rub(transaction)


def test_load_transactions_success():
    """Подготовим тестовые данные."""
    mock_data = [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]
    mock_file_path = "mock_transactions.json"

    # Используем mock_open для имитации открытия файла
    with patch("builtins.open", mock_open(read_data=json.dumps(mock_data))):
        # Убедитесь, что os.path.isfile возвращает True для mock_file_path
        with patch("os.path.isfile", return_value=True):
            result = load_transactions(mock_file_path)

    assert result == mock_data  # Проверяем, что данные загружены корректно


def test_load_transactions_file_not_exist():
    """Тестируем случай, когда файл не существует."""
    with patch("os.path.isfile", return_value=False):
        result = load_transactions("non_existent_file.json")
    assert result == []  # Проверяем, что результат пустой список


def test_load_transactions_invalid_json():
    """Тестируем случай с некорректным JSON."""
    with patch("builtins.open", mock_open(read_data='{"invalid_json": "data"')):  # Некорректный JSON
        with patch("os.path.isfile", return_value=True):
            result = load_transactions("mock_transactions.json")
    assert result == []  # Проверяем, что результат пустой список


def test_load_transactions_other_exception():
    """Тестируем случай, когда возникает другое исключение."""
    with patch("builtins.open", side_effect=IOError("File not accessible")):
        with patch("os.path.isfile", return_value=True):
            result = load_transactions("mock_transactions.json")
    assert result == []  # Проверяем, что результат пустой список


if __name__ == "__main__":
    pytest.main()
