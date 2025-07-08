"""Тест.

Проверяет функциональность декоратора.
"""

from src.decorators import my_function  # , log


def test_log(capsys):
    """Tecт."""
    my_function(12, 78)
    captured = capsys.readouterr()
    assert captured.out == "Function my_function called whith (12, 78) and kwargs {}. Result: 90\n"
