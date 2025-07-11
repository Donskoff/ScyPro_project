"""Тесты.

Модуля extermal_api.py.
"""

from unittest.mock import Mock, patch

from src.external_api import calculate_usd_to_rub, fetch_exchange_rates


@patch("src.external_api.requests.get")  # Патчим requests.get
def test_fetch_exchange_rates_success(mock_get):
    """Тестируем с помощью @patch."""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"rates": {"USD": 1.2, "RUB": 75.0}}
    mock_get.return_value = mock_response

    # Вызываем тестируемую функцию
    result = fetch_exchange_rates("http://data.fixer.io/api/latest", "dummy_access_key", "EUR", "USD,RUB")

    # Проверяем результат
    assert result == {"USD": 1.2, "RUB": 75.0}
    mock_get.assert_called_once_with(
        "http://data.fixer.io/api/latest",
        params={"access_key": "dummy_access_key", "base": "EUR", "symbols": "USD,RUB"},
    )


def test_calculate_usd_to_rub(calculate_usd_to_rub_fix):
    """Тест с фикстурой."""
    assert calculate_usd_to_rub(1, 2) == calculate_usd_to_rub_fix
