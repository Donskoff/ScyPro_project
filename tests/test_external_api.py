"""Тесты.

Модуля extermal_api.py.
"""

from unittest import mock

import pytest

from src.external_api import (convert_transaction_to_rub,  # Замените 'src.external_api' на правильный путь к вашему модулю
                              fetch_exchange_rates)


def test_fetch_exchange_rates_success(mocker):
    """Тест."""
    mock_response = {"rates": {"USD": 75.0, "RUB": 90.0}, "success": True}
    mocker.patch("requests.get", return_value=mock.Mock(status_code=200, json=lambda: mock_response))

    rates = fetch_exchange_rates("http://data.fixer.io/api/latest", "fake_api_key", "EUR", "USD,RUB")
    assert rates == {"USD": 75.0, "RUB": 90.0}


def test_fetch_exchange_rates_failure(mocker):
    """Тест."""
    mocker.patch("requests.get", return_value=mock.Mock(status_code=404))

    with pytest.raises(ValueError, match="Ошибка: 404"):
        fetch_exchange_rates("http://data.fixer.io/api/latest", "fake_api_key", "EUR", "USD,RUB")


def test_convert_transaction_to_rub_usd(mocker):
    """Тест."""
    mock_rates = {"USD": 75.0, "RUB": 90.0}
    mocker.patch("src.external_api.fetch_exchange_rates", return_value=mock_rates)  # Патчим fetch_exchange_rates

    transaction = {"operationAmount": {"amount": "100", "currency": {"code": "USD", "name": "USD"}}}

    result = convert_transaction_to_rub(transaction)
    assert result["operationAmount"]["amount"] == 120.0  # 100 * (90 / 75)
    assert result["operationAmount"]["currency"]["code"] == "RUB"
    assert result["operationAmount"]["currency"]["name"] == "руб."
