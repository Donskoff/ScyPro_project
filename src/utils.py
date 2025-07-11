"""Функция обработки транзакций.

Выводит данные о транзакциях из JSON-файла.
"""

import json
import os
from typing import Any, Dict, List


# def load_transactions(file_path: str) -> List[Dict[str, Any]]:
#     """Загружает данные о финансовых транзакциях из JSON-файла."""
#     # Проверяем, существует ли файл
#     if not os.path.isfile(file_path):
#         return []
#
#     # Открываем и читаем файл
#     try:
#         with open(file_path, encoding="utf-8") as file:
#             data = json.load(file)
#             # print(f"data = {data}")  # Добавьте этот вывод для отладки
#             # Проверяем, является ли данные списком
#             if isinstance(data, list):
#                 return data
#             else:
#                 return []
#     except json.JSONDecodeError:
#         # Если файл не содержит корректный JSON
#         return []
#     except Exception as e:
#         # Обработка других возможных исключений
#         print(f"An error occurred: {e}")
#         return []
#**************************************home
# import json
# import os
# from typing import Any, Dict, List
#
# def load_transactions(file_path: str) -> List[Dict[str, Any]]:
#     """Загружает данные о финансовых транзакциях из JSON-файла."""
#     if not os.path.isfile(file_path):
#         return []
#
#     try:
#         with open(file_path, encoding="utf-8") as file:
#             data = json.load(file)
#             return data if isinstance(data, list) else []
#     except (json.JSONDecodeError, OSError):
#         return []
#*******************************end
import json
import os
from typing import Any, Dict, List

def load_transactions(file_path: str) -> List[Dict[str, Any]]:
    """Загружает данные о финансовых транзакциях из JSON-файла."""
    if not os.path.isfile(file_path):
        return []

    with open(file_path, encoding="utf-8") as file:
        data = json.load(file)
        return data if isinstance(data, list) else []
#********************************************88888