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


def get_date(current_date_data: str) -> str:
    """Принимает на вход строку с датой в формате 2024-03-11T02:26:18.671407.

    И возвращает строку с датой в формате ДД.ММ.ГГГГ (11.03.2024).
    """
    formatted_date = (
        current_date_data[8]
        + current_date_data[9]
        + "."
        + current_date_data[5]
        + current_date_data[6]
        + "."
        + current_date_data[0]
        + current_date_data[1]
        + current_date_data[2]
        + current_date_data[3]
    )
    return formatted_date


bank_details_data = input("Введите данные банковской карты или счёта ... ")

output_data = mask_account_card(bank_details_data)
print(output_data)

date_data = "2025-03-12T02:26:18.671407"
print(get_date(date_data))
