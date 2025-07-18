"""Тест.

Проверяет функциональность декоратора.
"""

import logging

from src.decorators import my_function


# Убедитесь, что логирование настроено для захвата выводов в тестах
def setup_logging_for_tests():
    """Настройка логгирования."""
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def test_my_function(capsys):
    """Тестирует успешное выполнение функции и логирование."""
    setup_logging_for_tests()  # Настройка логирования для тестов

    result = my_function(1, 7)  # Вызов функции
    assert result == 8  # Проверка результата

    # Перехватываем вывод
    captured = capsys.readouterr()

    # Проверяем, что в выводе есть ожидаемые строки
    assert "Function my_function called whith (1, 7) and kwargs {}. Result: 8" in captured.out


def test_log(capsys):
    """Tecт."""
    my_function(12, 78)
    captured = capsys.readouterr()
    assert captured.out == "Function my_function called whith (12, 78) and kwargs {}. Result: 90\n"
