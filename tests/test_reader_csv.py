"""Тесты функций модуля operation_reader.py."""

import unittest
from unittest.mock import mock_open, patch

from src.operation_reader import reader_csv


class TestReaderCSV(unittest.TestCase):
    """
    Класс для тестирования функции reader_csv.

    Содержит тесты, проверяющие корректность обработки CSV-файлов,
    включая сценарии с отсутствующими файлами и пустыми файлами.
    """

    def test_file_not_found(self):
        """
        Тестирует обработку ошибки при попытке открыть несуществующий файл.

        Проверяет, что возникает исключение FileNotFoundError, если файл не найден.
        """
        # Тестируем, что FileNotFoundError возникает для несуществующего файла
        with self.assertRaises(FileNotFoundError):
            reader_csv("non_existing_file.csv")

    def test_empty_file(self):
        """
        Тестирует чтение пустого CSV-файла.

        Проверяет, что функция reader_csv возвращает пустой список при
        чтении пустого файла.
        """
        # Тестируем чтение пустого CSV-файла
        mock_csv_data = ""

        with patch("builtins.open", mock_open(read_data=mock_csv_data)), patch(
            "os.path.isfile", return_value=True
        ):  # Мокаем os.path.isfile
            result = reader_csv("dummy_path.csv")

        expected_output = []
        self.assertEqual(result, expected_output)


if __name__ == "__main__":
    unittest.main()
