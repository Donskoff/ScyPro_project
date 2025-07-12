"""Тесты.

Тестовые функции для модуля utils.py.
"""
import json
from unittest import mock

from src.utils import load_transactions


def test_load_transactions_invalid_json(mocker: mock.MagicMock) -> None:
    """Создаем некорректные данные."""
    mock_open = mock.mock_open(read_data="invalid json")

    with mock.patch("builtins.open", mock_open):
        result = load_transactions("fake_path.json")
        assert result == []


def test_load_transactions_file_not_found(mocker: mock.MagicMock) -> None:
    """Патчим os.path.isfile, чтобы он возвращал False."""
    with mock.patch("os.path.isfile", return_value=False):
        result = load_transactions("fake_path.json")
        assert result == []


def test_load_transactions_not_a_list(mocker: mock.MagicMock) -> None:
    """Создаем данные, которые не являются списком."""
    test_data = {"id": 1, "amount": 100}
    mock_open = mock.mock_open(read_data=json.dumps(test_data))

    with mock.patch("builtins.open", mock_open):
        result = load_transactions("fake_path.json")
        assert result == []


def test_load_transactions_other_exception(mocker: mock.MagicMock) -> None:
    """Патчим open, чтобы вызвать исключение."""
    mock_open = mock.mock_open()
    mock_open.side_effect = Exception("Some error")

    with mock.patch("builtins.open", mock_open):
        result = load_transactions("fake_path.json")
        assert result == []


def test_load_transactions_empty_file(mocker: mock.MagicMock) -> None:
    """Проверка, что функция возвращает пустой список, если файл пустой."""
    mock_open = mock.mock_open(read_data="")

    with mock.patch("builtins.open", mock_open):
        result = load_transactions("fake_path.json")
        assert result == []


def test_load_transactions_file_not_found1(mock_file_not_found: None) -> None:
    """Проверка, что функция возвращает пустой список, если файл не существует."""
    result = load_transactions("fake_path.json")
    assert result == []


def test_load_transactions_empty_file2(mock_empty_file: None) -> None:
    """Проверка, что функция возвращает пустой список, если файл пустой."""
    result = load_transactions("fake_path.json")
    assert result == []


def test_load_transactions_invalid_json3(mock_invalid_json: None) -> None:
    """Проверка, что функция возвращает пустой список, если JSON не является списком."""
    result = load_transactions("fake_path.json")
    assert result == []


def test_load_transactions_valid_json(mocker: mock.MagicMock) -> None:
    """Создаем тестовые данные."""
    test_data = [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]
    mock_open = mock.mock_open(read_data=json.dumps(test_data))

    # Патчим os.path.isfile, чтобы он всегда возвращал True
    mocker.patch("os.path.isfile", return_value=True)

    # Патчим open в builtins, чтобы использовать наш mock_open
    with mock.patch("builtins.open", mock_open):
        result = load_transactions("fake_path.json")
        assert result == test_data
