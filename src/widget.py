"""Программа обработки информации как о картах, так и о счетах."""

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(bank_details: str) -> str:
    """Функция маскировки номера банковского счета или карты.

    Функция принимает на вход номер счета или карты и возвращает его маску.
    Номер счета замаскирован и отображается в формате Счёт **XXXX, а номер карты
    замаскирован и отображается в формате Название карты XXXX XX** **** XXXX,
    где X — это цифра номера.
    """
    bank_details_list = bank_details.split()
    if (
        len(bank_details_list[-1]) == 20
        and bank_details_list[-1].isdigit()
        and ("Счет" in bank_details)
        or ("Счёт" in bank_details)
    ):
        bank_details_list[-1] = get_mask_account(bank_details_list[-1])
        new_bank_details = " ".join(bank_details_list)
        return new_bank_details
    elif len(bank_details_list[-1]) == 16 and bank_details_list[-1].isdigit():
        bank_details_list[-1] = get_mask_card_number(bank_details_list[-1])
        new_bank_details = " ".join(bank_details_list)
        return new_bank_details
    else:
        return "Введённые вами данные не корректны!"


def get_date(date_string: str) -> str:
    """Форматируем дату.

    Принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ" пример: "11.03.2024"
    """
    # Разделяем строку на дату и время
    date_part = date_string.split("T")[0]

    # Разделяем дату на год, месяц и день
    year, month, day = date_part.split("-")

    # Формируем новую строку в нужном формате
    formatted_date = f"{day}.{month}.{year}"
    # можно так formatted_date = day + '.' + month + '.' + year

    return formatted_date


# def get_date(date_str: str) -> str:
#     from datetime import datetime
#     dt = datetime.fromisoformat(date_str)
#     return dt.strftime("%d.%m.%Y")
#
# # Пример использования
# print(get_date("2024-05-18T02:26:18.671407"))  # Выведет: 11.03.2024