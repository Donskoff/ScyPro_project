"""Тесты функций.

Модуля decoder_xlsx_json.py.
"""

import unittest

from src.decoder_xlsx_json import decoder_xlsx_json


class TestDecoderXlsxJson(unittest.TestCase):
    """
    Класс для тестирования функции декодирования данных из формата XLSX в JSON.

    Содержит тесты, проверяющие корректность преобразования данных
    из XLSX-формата в структурированный JSON-формат, включая
    обработку различных сценариев, таких как отсутствие данных.
    """

    def setUp(self):
        """
        Подготавливает тестовые данные перед каждым тестом.

        Инициализирует список транзакций с различными значениями,
        включая None для проверки обработки отсутствующих данных.
        """
        self.transactions2 = [
            {
                "id": 368297,
                "state": "PENDING",
                "date": "2022-04-20T01:43:35Z",
                "amount": None,  # Установим None для проверки
                "currency_name": "Sol",
                "currency_code": "PEN",
                "from": "нет данных",
                "to": "Счет 73197209028710375773",
                "description": "Открытие вклада",
            },
            {
                "id": 72219,
                "state": "EXECUTED",
                "date": "2023-08-09T03:54:59Z",
                "amount": 28868.0,
                "currency_name": "Koruna",
                "currency_code": "CZK",
                "from": "нет данных",
                "to": "Счет 65771273382053145248",
                "description": "Открытие вклада",
            },
        ]

        self.expected_transactions1 = [
            {
                "id": 368297,
                "state": "PENDING",
                "date": "2022-04-20T01:43:35Z",
                "operationAmount": {
                    "amount": "0",  # Проверяем, что значение по умолчанию равно "0"
                    "currency": {"name": "Sol", "code": "PEN"},
                },
                "description": "Открытие вклада",
                "from": "нет данных",
                "to": "Счет 73197209028710375773",
            },
            {
                "id": 72219,
                "state": "EXECUTED",
                "date": "2023-08-09T03:54:59Z",
                "operationAmount": {
                    "amount": "28868",  # Проверяем, что значение корректно преобразовано
                    "currency": {"name": "Koruna", "code": "CZK"},
                },
                "description": "Открытие вклада",
                "from": "нет данных",
                "to": "Счет 65771273382053145248",
            },
        ]

    def test_decoder_xlsx_json(self):
        """
        Тестирует функцию decoder_xlsx_json на корректность преобразования данных.

        Проверяет, что преобразованные данные соответствуют ожидаемому формату.
        """
        result = decoder_xlsx_json(self.transactions2)
        self.assertEqual(result, self.expected_transactions1)


if __name__ == "__main__":
    unittest.main()
