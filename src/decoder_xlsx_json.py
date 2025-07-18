"""
Преобразует список словарей transactions2 в формат, аналогичный transactions1.

:param transactions2: Список словарей с транзакциями в исходном формате.
:return: Список словарей с транзакциями в новом формате.
"""

import pandas as pd  # Импортируем pandas


def decoder_xlsx_json(transactions2):
    """
    Преобразует список словарей transactions2 в формат, аналогичный transactions1.

    :param transactions2: Список словарей с транзакциями в исходном формате.
    :return: Список словарей с транзакциями в новом формате.
    """
    transactions1 = []

    for transaction in transactions2:
        # Создаем новый словарь для каждого элемента
        new_transaction = {
            "id": transaction["id"],
            "state": transaction["state"],
            "date": transaction["date"],
            "operationAmount": {
                "amount": (
                    str(int(transaction["amount"]))
                    if isinstance(transaction["amount"], (int, float)) and not pd.isna(transaction["amount"])
                    else "0"
                ),  # Устанавливаем значение по умолчанию
                "currency": {"name": transaction["currency_name"], "code": transaction["currency_code"]},
            },
            "description": transaction["description"],
            "from": transaction["from"],
            "to": transaction["to"],
        }

        transactions1.append(new_transaction)

    return transactions1
