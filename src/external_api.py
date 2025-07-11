"""Конвертация по последним курсам.

Конвертируем сумму из одной валюты в другую на основе последних курсов.
"""

import os
from typing import Dict

import requests
from dotenv import load_dotenv

# Загрузка переменных из .env-файла
load_dotenv()

# Получение значения переменной API_KEY из .env-файла
API_KEY = os.getenv("API_KEY")

# URL для запроса
url = "http://data.fixer.io/api/latest"
access_key = f"{API_KEY}"
base_currency = "EUR"
symbols = "USD,RUB"


def fetch_exchange_rates(url: str, access_key: str, base_currency: str, symbols: str) -> Dict[str, float]:
    """Получает курсы валют из API."""
    response = requests.get(url, params={"access_key": access_key, "base": base_currency, "symbols": symbols})

    if response.status_code == 200:
        data = response.json()
        return {"USD": data["rates"]["USD"], "RUB": data["rates"]["RUB"]}
    else:
        raise ValueError(f"Ошибка: {response.status_code}")


def convert_transaction_to_rub(transaction: dict) -> dict:
    """Извлекаем сумму и валюту."""
    amount = float(transaction["operationAmount"]["amount"])
    currency_code = transaction["operationAmount"]["currency"]["code"]

    # Конвертируем сумму в рубли
    if currency_code != "RUB":
        # Получаем курсы валют
        rates = fetch_exchange_rates(url, access_key, base_currency, symbols)

        value_usd = rates["USD"]
        value_rub = rates["RUB"]

        if currency_code == "USD":
            transaction["operationAmount"]["amount"] = amount * value_rub / value_usd  # Конвертация в рубли
            transaction["operationAmount"]["currency"]["code"] = "RUB"
            transaction["operationAmount"]["currency"]["name"] = "руб."
        elif currency_code == "EUR":
            transaction["operationAmount"]["amount"] = amount * value_rub  # Конвертация в рубли
            transaction["operationAmount"]["currency"]["code"] = "RUB"
            transaction["operationAmount"]["currency"]["name"] = "руб."
        else:
            return transaction
    return transaction
