"""Этот модуль содержит функции для работы с масками."""

import logging
import os

# Создаем директорию для логов, если она не существует
log_dir = "C:/Users/bione/Desktop/my_prj/my_home_project/logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Настройка логгера
logger_mask = logging.getLogger(__name__)
logger_mask.setLevel(logging.DEBUG)  # Устанавливаем уровень логирования

# Создаем обработчик для записи логов в файл
file_handler = logging.FileHandler(os.path.join(log_dir, "log_utils.log"), encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)

# Добавляем обработчик к логгеру
logger_mask.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера банковской карты.

    Функция принимает на вход номер карты и возвращает её маску.
    Номер карты замаскирован и отображается в формате XXXX XX** **** XXXX.
    """
    logger_mask.info(f"Получен номер карты: {card_number}")

    # Убираем все пробелы
    number_without_spaces = card_number.replace(" ", "")
    logger_mask.info(f"Номер карты без пробелов: {number_without_spaces}")

    # Проверяем, что длина номера карты корректная
    if len(number_without_spaces) != 16 or not number_without_spaces.isdigit():
        logger_mask.warning("Введён некорректный номер карты")
        return "Введён некорректный номер карты"

    # Форматируем по блокам по 4 цифры с пробелами
    masked_card_number = " ".join(number_without_spaces[i: i + 4] for i in range(0, len(number_without_spaces), 4))
    logger_mask.info(f"Форматированный номер карты: {masked_card_number}")

    # Преобразуем строку в список
    masked_card_number_list = list(masked_card_number)
    for i in range(len(masked_card_number_list)):
        if 7 <= i <= 13 and masked_card_number_list[i] != " ":
            # Заменяем символ на "*"
            masked_card_number_list[i] = "*"

    # Преобразуем список обратно в строку
    masked_card_number = "".join(masked_card_number_list)
    logger_mask.info(f"Замаскированный номер карты: {masked_card_number}")

    return masked_card_number


def get_mask_account(account_number: str) -> str:
    """Функция маскировки номера банковского счета.

    Функция принимает на вход номер счета и возвращает его маску.
    Номер счета замаскирован и отображается в формате **XXXX, где X — это цифра номера.
    То есть видны только последние 4 цифры номера, а перед ними — две звездочки.
    """
    logger_mask.info(f"Получен номер счета: {account_number}")

    # Убираем все пробелы
    count_without_spaces = account_number.replace(" ", "")
    logger_mask.info(f"Номер счета без пробелов: {count_without_spaces}")

    # Проверяем, что длина номера счета корректная
    if len(count_without_spaces) != 20 or not count_without_spaces.isdigit():
        logger_mask.warning("Некорректный номер счёта")
        return "Некорректный номер счёта"

    # Преобразуем строку в список
    count_without_spaces_list = list(count_without_spaces)
    logger_mask.info(f"Список символов номера счета: {count_without_spaces_list}")

    for i in range(len(count_without_spaces_list)):
        if 0 <= i <= 13:
            count_without_spaces_list[i] = ""
        elif 13 < i < 16:
            count_without_spaces_list[i] = "*"

    # Преобразуем список обратно в строку
    masked_account_number = "".join(count_without_spaces_list)
    logger_mask.info(f"Замаскированный номер счета: {masked_account_number}")

    return masked_account_number
