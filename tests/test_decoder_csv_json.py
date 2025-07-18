"""Тесты функции decoder_csv_json.py."""

import unittest

from src.decoder_csv_json import decoder_csv_json


class TestDecoderCSVJson(unittest.TestCase):
    """
    Класс для тестирования функции decoder_csv_json.

    Содержит тесты, проверяющие корректность преобразования данных
    из CSV-формата в структурированный JSON-формат.
    """

    def test_valid_data(self):
        """Тестирует функцию decoder_csv_json на корректных данных.

        Проверяет, правильно ли функция преобразует список словарей с
        CSV-форматированными строками в структурированный список словарей
        транзакций с соответствующими атрибутами.
        """
        data = [
            {
                "id;state;date;amount;currency_name;currency_code;from;to;description":
                    "650703;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;Счет 58803664561298323391;"
                    "Счет 39745660563456619397;Перевод организации"
            },
            {
                "id;state;date;amount;currency_name;currency_code;from;to;description":
                    "3598919;EXECUTED;2020-12-06T23:00:58Z;29740;Peso;COP;Discover 3172601889670065;"
                    "Discover 0720428384694643;"
                    "Перевод с карты на карту"
            },
        ]
        expected_output = [
            {
                "id": 650703,
                "state": "EXECUTED",
                "date": "2023-09-05T11:30:32Z",
                "operationAmount": {"amount": "16210", "currency": {"name": "Sol", "code": "PEN"}},
                "description": "Перевод организации",
                "from": "Счет 58803664561298323391",
                "to": "Счет 39745660563456619397",
            },
            {
                "id": 3598919,
                "state": "EXECUTED",
                "date": "2020-12-06T23:00:58Z",
                "operationAmount": {"amount": "29740", "currency": {"name": "Peso", "code": "COP"}},
                "description": "Перевод с карты на карту",
                "from": "Discover 3172601889670065",
                "to": "Discover 0720428384694643",
            },
        ]
        result = decoder_csv_json(data)
        self.assertEqual(result, expected_output)

    def test_none_input(self):
        """
        Тестирует функцию decoder_csv_json на входе None.

        Проверяет, что функция возвращает пустой список при передаче
        значения None.
        """
        data = None
        expected_output = []
        result = decoder_csv_json(data)
        self.assertEqual(result, expected_output)

    def test_empty_string(self):
        """
        Тестирует функцию decoder_csv_json на пустой строке.

        Проверяет, что функция возвращает пустой список при передаче
        пустой строки в формате CSV.
        """
        data = [{"id;state;date;amount;currency_name;currency_code;from;to;description": ""}]
        expected_output = []
        result = decoder_csv_json(data)
        self.assertEqual(result, expected_output)

    def test_empty_id(self):
        """
        Тестирует функцию decoder_csv_json на пустом идентификаторе.

        Проверяет, что функция возвращает пустой список, если
        идентификатор транзакции отсутствует в строке.
        """
        data = [
            {
                "id;state;date;amount;currency_name;currency_code;from;to;description": ";\
                EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;Счет 58803664561298323391;\
                Счет 39745660563456619397;Перевод организации"
            }
        ]
        expected_output = []
        result = decoder_csv_json(data)
        self.assertEqual(result, expected_output)


if __name__ == "__main__":
    unittest.main()
