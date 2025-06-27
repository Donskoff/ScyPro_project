"""Этот модуль содержит функции обработки данных filter_by_state и sort_by_date."""

from datetime import datetime


def filter_by_state(operations: list[dict], state: str = "EXECUTED", sort: bool = True) -> list[dict]:
    """Функция фильтрации списка.

    Принимает список словарей и опционально значение для ключа
    state(по умолчанию 'EXECUTED'). Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению
    """
    # Фильтруем операции по состоянию
    filtered_operations = [operation for operation in operations if operation.get("state") == state]

    # Сортируем операции по дате
    # Для этого необходимо гарантировать, что ключ 'date' есть в каждом словаре и он в правильном формате
    if sort:
        filtered_operations.sort(key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"), reverse=True)
    else:
        filtered_operations.sort(key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"))

    return filtered_operations


# Пример использования функции:
# if __name__ == "__main__":
#     operations = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#                   {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
#                   {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#                   {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
#
#     result = filter_by_state(operations)
#     print("filter_by_state")
#     print(result)


def sort_by_date(filter_operations: list[dict], sort: bool = True) -> list[dict]:
    """Функция сортировки списка.

    Принимает список словарей и необязательный параметр, задающий порядок сортировки
    (по умолчанию 'True' — убывание). Функция должна возвращать новый список, отсортированный по дате (date).
    """
    # Сортируем операции по дате
    if sort:
        sorted_operations = sorted(
            filter_operations, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"), reverse=True
        )
    else:
        sorted_operations = sorted(
            filter_operations, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f")
        )

    return sorted_operations


# Пример использования функции:
# if __name__ == "__main__":
#     operations = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#                   {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
#                   {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#                   {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

# Фильтруем операции, например, только с состоянием EXECUTED
# filter_operations = [operation for operation in operations if operation.get('state') == 'EXECUTED']

# Сортируем отфильтрованные операции
# sorted_operations = sort_by_date(filter_operations)
# sorted_operations = sort_by_date(operations)
# print("sorted_operations")
# print(sorted_operations)
