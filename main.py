"""Функция основной логики функционала проекта.

Отвечает за основную логику проекта и связывает функциональности между собой.
"""

from src.decoder_csv_json import decoder_csv_json
from src.decoder_xlsx_json import decoder_xlsx_json
from src.operation_reader import reader_csv, reader_xlsx
from src.utils import load_transactions

file_path_json = r"C:\Users\bione\Desktop\my_prj\my_home_project\data\operations.json"
file_path_csv = r"C:\Users\bione\Desktop\my_prj\my_home_project\data\transactions.csv"
file_path_xlsx = r"C:\Users\bione\Desktop\my_prj\my_home_project\data\transactions_excel.xlsx"


def main():
    """Функция основной логики функционала проекта."""
    print(
        "Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n"
        "Выберите необходимый пункт меню:\n"
        "1. Получить информацию о транзакциях из JSON-файла\n"
        "2. Получить информацию о транзакциях из CSV-файла\n"
        "3. Получить информацию о транзакциях из XLSX-файла\n"
    )

    menu_options = {
        "1": "Для обработки выбран JSON-файл\n",
        "2": "Для обработки выбран CSV-файл\n",
        "3": "Для обработки выбран XLSX-файл\n",
    }

    while True:
        num_menu = input("Выберите необходимый пункт меню: введите цифру 1, 2 или 3 = ")

        if num_menu in menu_options:
            print(menu_options[num_menu])
            num = int(num_menu)
            if num == 1:
                # функция выводит список словарей о транзакциях из .JSON
                data = load_transactions(file_path_json)
                break  # Выход из цикла
            elif num == 2:
                data_csv = reader_csv(file_path_csv)
                data = decoder_csv_json(data_csv)
                break  # Выход из цикла
            else:
                data_xlsx = reader_xlsx(file_path_xlsx)
                data = decoder_xlsx_json(data_xlsx)
                break  # Выход из цикла
        else:
            try:
                num = int(num_menu)
                print(f"Ошибка! Вы ввели числовое значение = {num} не из требуемого диапазона 1, 2, 3\n")
            except ValueError:
                print("Ошибка: введено не числовое значение!!!\n")

    while True:
        status = input(
            "Введите статус, по которому необходимо выполнить фильтрацию.\n"
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING "
        ).upper()
        if status in ["EXECUTED", "CANCELED", "PENDING"]:
            # Фильтрация по ключу "state" с заданным значением
            # age_to_filter = status
            filtered_data = [transaction for transaction in data if transaction.get("state") == status]
            print(filtered_data)
            break
        else:
            print(f"Статус операции '{status}' недоступен.\n")

    while True:
        sort_date = input("Отсортировать операции по дате? Да/Нет  ").upper()

        if sort_date == "ДА":
            direction = input("Отсортировать операции по возрастанию - 'Да' или убыванию - 'Нет'?  ").upper()
            if direction == "ДА":
                filtered_data = sorted(filtered_data, key=lambda x: x["date"], reverse=False)
                print(f"Вывод отсортированного списка по возрастанию даты:\n{filtered_data}")
                break
            elif direction == "НЕТ":
                filtered_data = sorted(filtered_data, key=lambda x: x["date"], reverse=True)
                print(f"Вывод отсортированного списка по убыванию даты:\n{filtered_data}")
                break
        elif sort_date == "НЕТ":
            break
        else:
            print("Неверно введены данные !!! ")

    print("Переходим к сортировке по валюте.")
    if filtered_data:  # Проверяем, что список не пуст
        filter_choice = input("Выводить только рублевые транзакции? Да/Нет?  ").upper()
        if filter_choice == "ДА":
            # Фильтрация по ключу с заданным значением 'currency': {'name': 'руб', 'code': 'RUB'}
            age_to_filter = "RUB"

            # Фильтрация по вложенным ключам
            filtered_data = [
                transaction
                for transaction in filtered_data
                if transaction.get("operationAmount", {}).get("currency", {}).get("code") == age_to_filter
            ]
            print(f"Выводим только рублевые транзакции:\n {filtered_data}")
        else:
            print("Будет выводиться список транзакций по всем валютам.")
        if not filtered_data == []:
            # print(f"Выводим только рублевые транзакции:\n {filtered_data}")
            ans = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет  ").upper()
            if ans == "ДА":
                age_to_filter = input(
                    "Введите выражение из представленных для фильтрации:\n\
1.Перевод с карты на карту\n2.Перевод организации\n3.Открытие вклада   "
                )
                print(f"age_to_filter =  {age_to_filter}")
                filtered_data = [item for item in filtered_data if item.get("description") == age_to_filter]
            else:
                print("Будет выводиться список транзакций по всем описаниям.")

            print(f"Выводим окончательный список.\n {filtered_data}")
            # ******************
            if filtered_data:  # Проверяем, что filtered_data не пуст
                print(f"Всего банковских операций в выборке: {len(filtered_data)}\n")

                for item in filtered_data:
                    # Используем get() для безопасного доступа к ключам
                    date = item.get("date", "Дата не указана")
                    description = item.get("description", "Описание не указано")
                    # from_account = item.get("from", "Откуда не указано")
                    from_ = item.get("from", "Откуда не указано")
                    to_ = item.get("to", "Куда не указано")
                    amount = item.get("operationAmount", {}).get("amount", "Сумма не указана")
                    currency_name = (
                        item.get("operationAmount", {}).get("currency", {}).get("name", "Валюта не указана")
                    )
                    print(f"{date}  {description}")
                    print(f"{from_} -> {to_}")
                    print(f"Сумма: {amount} {currency_name}\n")
            else:
                print("Не найдено ни одной транзакции.")
        else:
            print("Не найдено ни одной транзакции.")


if __name__ == "__main__":
    main()
