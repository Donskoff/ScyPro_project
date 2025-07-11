"""Функции обработки транзакций.

Обрабатывают транзакции.
"""

import json
import os
from src.external_api import value_rub_usd, value_rub
from typing import List, Dict, Any

def load_transactions(file_path: str) -> List[Dict[str, Any]]:
    """Загружает данные о финансовых транзакциях из JSON-файла."""
    # Проверяем, существует ли файл
    if not os.path.isfile(file_path):
        return []

    # Открываем и читаем файл
    try:
        with open(file_path, encoding="utf-8") as file:
            data = json.load(file)

            # Проверяем, является ли данные списком
            if isinstance(data, list):
                return data
            else:
                return []
    except json.JSONDecodeError:
        # Если файл не содержит корректный JSON
        return []
    except Exception as e:
        # Обработка других возможных исключений
        print(f"An error occurred: {e}")
        return []
#************************************************************
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
#             if isinstance(data, list):
#                 return data
#             return []
#     except json.JSONDecodeError:
#         return []
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         return []
#************************************************************
# Путь к файлу operations.json
file_path = r"C:\Users\bione\Desktop\my_prj\my_home_project\data\operations.json"

transactions = load_transactions(file_path)
# print(transactions)
# print(external_api.value_rub_usd)
# print(external_api.value_rub)


def convert_transaction_to_rub(transaction: Dict[str, Any]) -> Dict[str, Any]:
    """Извлекаем сумму и валюту."""
    amount = float(transaction["operationAmount"]["amount"])
    currency_code = transaction["operationAmount"]["currency"]["code"]

    # Конвертируем сумму в рубли
    if currency_code == "RUB":
        transaction["operationAmount"]["amount"] = amount  # Сумма уже в рублях
    elif currency_code == "USD":
        transaction["operationAmount"]["amount"] = amount * value_rub_usd  # Конвертация в рубли
        transaction["operationAmount"]["currency"]["code"] = "RUB"
        transaction["operationAmount"]["currency"]["name"] = "руб."
    elif currency_code == "EUR":
        transaction["operationAmount"]["amount"] = amount * value_rub  # Конвертация в рубли
        transaction["operationAmount"]["currency"]["code"] = "RUB"
        transaction["operationAmount"]["currency"]["name"] = "руб."
    else:
        raise ValueError(f"Неизвестная валюта: {currency_code}")

    return transaction

#*********************потом это надо раскоментировать
# Пример транзакции
transaction = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {"amount": "31957.58", "currency": {"name": "USD", "code": "USD"}},
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589",
}

# Использование функции
try:
    modified_transaction = convert_transaction_to_rub(transaction)
    print(modified_transaction)
except ValueError as e:
    print(e)
