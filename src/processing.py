"""Этот модуль содержит функции обработки данных filter_by_state и sort_by_date."""

from datetime import datetime


def filter_by_state(operations: list[dict], state: str = "EXECUTED") -> list[dict] | None:
    """Функция фильтрации списка.

    Принимает список словарей и опционально значение для ключа
    state(по умолчанию 'EXECUTED'). Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению
    """
    # Фильтруем операции по состоянию
    filtered_operations = [operation for operation in operations if operation.get("state") == state]
    return filtered_operations


def sort_by_date(operations: list[dict], reverse: bool = True) -> list[dict]:
    """Функция сортировки списка.

    Принимает список словарей и необязательный параметр, задающий порядок сортировки
    (по умолчанию 'True' — убывание). Функция должна возвращать новый список, отсортированный по дате (date).
    """
    return sorted(operations, key=lambda x: datetime.fromisoformat(x["date"]), reverse=reverse)
