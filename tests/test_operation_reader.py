"""Тестирование.

Функций reader_csv(file_path) и .
"""

import unittest
from unittest.mock import mock_open, patch

import pandas as pd

from src.operation_reader import reader_csv, reader_xlsx


class TestReaderXlsx(unittest.TestCase):
    """
    Тестирование функции reader_csv(file_path).

    Этот класс содержит тесты для функции reader_csv,
    которая считывает финансовые операции из файла transactions.csv.
    Тесты проверяют:

    1. Успешное считывание данных из корректного CSV-файла.
    2. Обработку случая, когда файл не найден.
    3. Обработку пустого файла.
    """

    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data="date,amount,description\n2023-01-01,100,Deposit\n2023-01-02,-50,Withdrawal\n",
    )
    def test_reader_csv_success(self, mock_file):
        """Тестирование успешного считывания данных из CSV."""
        file_path = "data/transactions.csv"
        expected_output = [
            {"date": "2023-01-01", "amount": "100", "description": "Deposit"},
            {"date": "2023-01-02", "amount": "-50", "description": "Withdrawal"},
        ]

        result = reader_csv(file_path)

        self.assertEqual(result, expected_output)
        mock_file.assert_called_once_with(file_path, mode="r", encoding="utf-8")

    @patch("os.path.isfile", return_value=False)
    def test_reader_csv_file_not_found(self, mock_isfile):
        """Тестирование обработки отсутствия файла."""
        file_path = "data/transactions.csv"

        with self.assertRaises(FileNotFoundError) as context:
            reader_csv(file_path)

        self.assertEqual(str(context.exception), f"Файл не найден: {file_path}")

    @patch("builtins.open", new_callable=mock_open)
    def test_reader_csv_empty_file(self, mock_file):
        """Тестирование считывания пустого файла."""
        mock_file.return_value.read = ""
        file_path = "data/transactions.csv"

        result = reader_csv(file_path)

        self.assertEqual(result, [])
        mock_file.assert_called_once_with(file_path, mode="r", encoding="utf-8")

    @patch("src.operation_reader.pd.read_excel")
    def test_reader_xlsx(self, mock_read_excel):
        """Подготовка тестовых данных."""
        mock_data = {
            "date": ["2021-01-01", "2021-01-02"],
            "amount": [100.0, -50.0],
            "description": ["Deposit", "Withdrawal"],
        }
        mock_df = pd.DataFrame(mock_data)
        mock_read_excel.return_value = mock_df

        # Путь к файлу (можно использовать любой, так как мы мокируем чтение)
        file_path = "C:/Users/bione/Desktop/my_prj/my_prj/my_home_project/data/transactions_excel.xlsx"

        # Вызов тестируемой функции
        result = reader_xlsx(file_path)

        # Ожидаемый результат
        expected_result = [
            {"date": "2021-01-01", "amount": 100.0, "description": "Deposit"},
            {"date": "2021-01-02", "amount": -50.0, "description": "Withdrawal"},
        ]

        # Проверка результата
        self.assertEqual(result, expected_result)
        mock_read_excel.assert_called_once_with(file_path)

    @patch("src.operation_reader.pd.read_excel")
    def test_reader_xlsx_empty_file(self, mock_read_excel):
        """Подготовка пустого DataFrame."""
        mock_df = pd.DataFrame(columns=["date", "amount", "description"])
        mock_read_excel.return_value = mock_df

        file_path = "C:/Users/bione/Desktop/my_prj/my_prj/my_home_project/data/transactions_excel.xlsx"

        # Вызов тестируемой функции
        result = reader_xlsx(file_path)

        # Ожидаемый результат - пустой список
        expected_result = []

        # Проверка результата
        self.assertEqual(result, expected_result)
        mock_read_excel.assert_called_once_with(file_path)


if __name__ == "__main__":
    unittest.main()
