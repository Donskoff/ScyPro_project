"""Содержит тесты, проверяющие корректность обработки банковских операций.

Включает различные сценарии, такие как пустые данные,
отсутствие совпадений с категориями и нечувствительность к регистру.
"""

import unittest

from src.process_searching import process_bank_operations  # Замените your_module на имя вашего модуля


class TestProcessBankOperations(unittest.TestCase):
    """
    Класс для тестирования функции process_bank_operations.

    Содержит тесты, проверяющие корректность обработки банковских операций
    по категориям, включая различные сценарии, такие как пустые данные,
    отсутствие совпадений с категориями и нечувствительность к регистру.
    """

    def setUp(self):
        """
        Подготавливает тестовые данные перед каждым тестом.

        Инициализирует список транзакций и категории для использования в тестах.
        """
        self.data = [
            {"id": 1, "description": "Оплата за интернет"},
            {"id": 2, "description": "Перевод на карту"},
            {"id": 3, "description": "Оплата коммунальных услуг"},
            {"id": 4, "description": "Покупка в магазине"},
            {"id": 5, "description": "Оплата за мобильную связь"},
            {"id": 6, "description": "Перевод организации"},
        ]
        self.categories = ["Оплата", "Перевод", "Покупка"]

    def test_process_bank_operations(self):
        """
        Тестирует функцию process_bank_operations на корректных данных.

        Проверяет, правильно ли функция подсчитывает количество операций
        по заданным категориям.
        """
        result = process_bank_operations(self.data, self.categories)
        expected = {"Оплата": 3, "Перевод": 2, "Покупка": 1}
        self.assertEqual(result, expected)

    def test_empty_data(self):
        """
        Тестирует функцию process_bank_operations на пустых данных.

        Проверяет, что функция возвращает нулевые значения для всех категорий
        при передаче пустого списка транзакций.
        """
        result = process_bank_operations([], self.categories)
        expected = {"Оплата": 0, "Перевод": 0, "Покупка": 0}
        self.assertEqual(result, expected)

    def test_no_matching_categories(self):
        """
        Тестирует функцию process_bank_operations при отсутствии совпадений.

        Проверяет, что функция возвращает нулевое значение для категории,
        которая не присутствует в данных.
        """
        result = process_bank_operations(self.data, ["Тест"])
        expected = {"Тест": 0}
        self.assertEqual(result, expected)

    def test_case_insensitivity(self):
        """
        Тестирует функцию process_bank_operations на нечувствительность к регистру.

        Проверяет, что функция корректно обрабатывает категории независимо
        от регистра символов.
        """
        result = process_bank_operations(self.data, ["оплата", "ПЕРЕВОД"])
        expected = {"оплата": 3, "ПЕРЕВОД": 2}
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
