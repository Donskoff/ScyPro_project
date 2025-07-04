"""Этот модуль содержит функции для работы с масками."""


def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера банковской карты.

    Функция принимаeт на вход номер карты и возвращает её маску.
    Номер карты замаскирован и отображается в формате XXXX XX** **** XXXX.
    """
    # Убираем все пробелы
    number_without_spaces = card_number.replace(" ", "")
    # Проверяем, что длина номера карты корректная
    if len(number_without_spaces) != 16 or not number_without_spaces.isdigit():
        return "Введён некорректный номер карты"
    # Форматируем по блокам по 4 цифры с пробелами
    masked_card_number = " ".join(number_without_spaces[i: i + 4] for i in range(0, len(number_without_spaces), 4))
    # Преобразуем строку в список
    masked_card_number_list = list(masked_card_number)
    for i in range(len(masked_card_number_list)):
        if 7 <= i <= 13 and masked_card_number_list[i] != " ":
            # Заменяем символ на "*"
            masked_card_number_list[i] = "*"
    # Преобразуем список обратно в строку
    masked_card_number = "".join(masked_card_number_list)
    return masked_card_number


def get_mask_account(account_number: str) -> str:
    """Функция маскировки номера банковского счета.

    Функция принимает на вход номер счета и возвращает его маску.
    Номер счета замаскирован и отображается в формате **XXXX, где X — это цифра номера.
    То есть видны только последние 4 цифры номера, а перед ними — две звездочки.
    """
    # Убираем все пробелы
    count_without_spaces = account_number.replace(" ", "")
    if len(count_without_spaces) != 20 or not count_without_spaces.isdigit():
        return "Некорректный номер счёта"
    # Преобразуем строку в список
    count_without_spaces_list = list(count_without_spaces)
    for i in range(len(count_without_spaces_list)):
        if 0 <= i <= 13:
            # Заменяем символ на "*"
            count_without_spaces_list[i] = ""
        elif 13 < i < 16:
            count_without_spaces_list[i] = "*"
        # Преобразуем список обратно в строку
    masked_account_number = "".join(count_without_spaces_list)
    return masked_account_number
