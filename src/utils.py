"""Функция обработки транзакций.

Выводит данные о транзакциях из JSON-файла.
"""

import json
import logging
import os
from typing import Any, Dict, List

# Создаем директорию для логов, если она не существует
log_dir = "C:/Users/bione/Desktop/my_prj/my_home_project/logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Настройка логгера
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  # Устанавливаем уровень логирования

# Создаем обработчик для записи логов в файл
file_handler = logging.FileHandler(os.path.join(log_dir, "log_utils.log"), encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)

# Добавляем обработчик к логгеру
logger.addHandler(file_handler)


def load_transactions(file_path: str) -> List[Dict[str, Any]]:
    """Загружает данные о финансовых транзакциях из JSON-файла."""
    logger.info(f"Попытка загрузить транзакции из: {file_path}")

    if not os.path.isfile(file_path):
        logger.warning(f"Загружаемый файл не определён: {file_path}")
        return []

    logger.info(f"Файл найден. Открытие файла: {file_path}")

    with open(file_path, encoding="utf-8") as file:
        data = json.load(file)
        logger.info("Данные успешно загружены.")

        if isinstance(data, list):
            logger.info("Возвращается список данных.")
            return data
        else:
            logger.warning("Данные не являются списком, возвращается пустой список.")
            return []
