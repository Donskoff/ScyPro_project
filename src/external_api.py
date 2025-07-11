"""Конвертация по последним курсам.

Конвертируем сумму из одной валюты в другую на основе последних курсов.
"""

import os
import requests
from typing import Dict
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

    # data = response.json()
    # return {"USD": data["rates"]["USD"], "RUB": data["rates"]["RUB"]}

def calculate_usd_to_rub(value_rub: float, value_usd: float) -> float:
    """Конвертирует рубли в доллары по курсу."""
    return value_rub / value_usd


# # Получаем курсы валют
try:
    rates = fetch_exchange_rates(url, access_key, base_currency, symbols)
    value_usd = rates["USD"]
    value_rub = rates["RUB"]
    value_rub_usd = calculate_usd_to_rub(value_rub, value_usd)

    # Выводим курсы
    print(f"Курс EUR к USD: {value_usd}")
    print(f"Курс EUR к RUB: {value_rub}")
    print(f"Курс USD к RUB: {value_rub_usd}")

except ValueError as e:
    print(e)
# print(os.path.abspath("src/external_api.py"))