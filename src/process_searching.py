"""Функции поиска.

Функция выборки из списков словарей по заданным параметрам.
"""

import re
from typing import Dict, List


def process_bank_operations(data: List[Dict], categories: List[str]) -> Dict[str, int]:
    """
    Функция для подсчета количества банковских операций по категориям.

    :param data: Список словарей, где каждый словарь представляет банковскую операцию.
    :param categories: Список категорий для подсчета операций.
    :return: Словарь, где ключи — названия категорий, а значения — количество операций в каждой категории.
    """
    # Инициализируем словарь для хранения результатов
    category_count = {category: 0 for category in categories}

    # Обрабатываем каждую операцию
    for operation in data:
        description = operation.get("description", "")
        # Проверяем каждую категорию
        for category in categories:
            # Используем регулярное выражение для поиска категории в описании
            if re.search(re.escape(category), description, re.IGNORECASE):
                category_count[category] += 1

    return category_count
