"""Считывает финансовые операции.

Из файлов transactions.csv и transactions_excel.xlsx.
"""

import csv
import os
from typing import Dict, List

import pandas as pd


def reader_csv(file_path: str) -> List[Dict[str, str]]:
    """
    Считывает финансовые операции из файла transactions.csv.

    Аргументы:
    file_path -- путь к файлу transactions.csv

    Возвращает:
    Список словарей с транзакциями.
    """
    transactions = []
    # Проверяем, существует ли файл
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Файл не найден: {file_path}")

    with open(file_path, mode="r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            transactions.append(row)

    return transactions


def reader_xlsx(file_path_xlsx):
    """
    Считывает финансовые операции из файла Excel и возвращает их в виде списка словарей.

    :param file_path_xlsx: Путь к файлу Excel.
    :return: Список словарей с транзакциями.
    """
    # Чтение данных из Excel файла
    df = pd.read_excel(file_path_xlsx)

    # Замена NaN на "нет данных"
    df.fillna("нет данных", inplace=True)

    # Преобразование DataFrame в список словарей
    transactions = df.to_dict(orient="records")
    # Ключ, по которому нужно изменить значение
    key_to_change = "id"

    # Изменение значений float на целочисленные
    for transaction in transactions:
        if key_to_change in transaction and isinstance(transaction[key_to_change], float):
            transaction[key_to_change] = int(transaction[key_to_change])
    return transactions
