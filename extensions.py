import requests  # импортируем наш знакомый модуль
import json
from config import currencies


class Convert:

    @staticmethod
    def get_price(base, quote, amount):
        # данные из cbs: словарь, стоимость всех валют в рублях.
        # Курса рубля там нет, буду добавлять в ручную равным 1
        # Обнавляется раз в сутки

        if base == quote:
            raise APIException(f"Не хочу переводить одинаковые валюты <b>{base}</b>")

        try:
            base_ticker = currencies[base]
        except KeyError:
            raise APIException(f"Не найдена валюта <b>{base}</b>\n/values")

        try:
            quote_ticker = currencies[quote]
        except KeyError:
            raise APIException(f"Не найдена валюта <b>{quote}</b>\n/values")

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f"Сумма <b>{amount}</b> указанна не верно\n/help")

        json_obj = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")  # Загружаем данные
        rates = json.loads(json_obj.content)['Valute']  # преобразуем в словарь
        rates.update({'RUB': {"Value": 1}})  # добавляем рубль равный 1 рубль
        return round(rates[base_ticker]['Value'] / rates[quote_ticker]['Value'] * amount, 2)
        # Формула изменится для валют, стоимость которых указанна за 10 или 100 единиц .get(Nominal)


class APIException(Exception):
    pass
