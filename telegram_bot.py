import telebot
from config import TOKEN
from extensions import *

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_start(message):
    bot.reply_to(message, "\
Здравствуйте\n\
Курс валюты ЦБ\n\
вам доступны команды:\n\
/help, /start, /values\n\
")


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "\
Вам доступны команды:\n\
/help, /start, /values\n\
Формат запроса:\n\
валюта_1 валюта_2 сумма\
")


@bot.message_handler(commands=['values'])
def send_values(message):
    bot.reply_to(message, "Список валюты:\n- " + '\n- '.join(currencies.keys()))


# Обрабатываются все сообщения
@bot.message_handler(content_types=['text'])
def handle_docs_audio(message):
    try:
        list_text = message.text.split()
        if len(list_text) != 3:  # упращенная проверка колличества параметров
            raise APIException(f'Неверное количество параметров\n/help')

        base, quote, amount = list_text

        result_amount = Convert.get_price(base, quote, amount)
        text = f"{amount} {base} == <b>{result_amount}</b> {quote}"
        bot.send_message(message.chat.id, text, parse_mode="HTML")
    except APIException as e:
        text = f'Ошибка ввода:\n{str(e)}'
        bot.reply_to(message, text, parse_mode="HTML")


bot.polling(none_stop=True)
