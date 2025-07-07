"""Тест.

Проверяет функциональность декоратора.
"""

from src.decorators import log


@log()
def test_log(capsys):
    """Tecт."""
    log()
    captured = capsys.readouterr()
    assert captured.out == "Starting my_function with args: (115, 118), kwargs: {}"
    assert captured.out == "my_function ok. Result: 233"
