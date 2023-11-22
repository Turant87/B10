import telebot
from ParsingCurrency import *


TOKEN = "6355423357:AAFTglngUhfzEIHHMlBgJfnJmRXnXxGeMCA"

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Приветствую! ' + str(message.chat.first_name)) # send_message - отправка сообщения в чат
    bot.send_message(message.chat.id, 'Введите /help, что бы узнать чем я могу Вам помочь ')

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, 'Я бот и я умею всякое') # replay_to - ответ с цитатой
    bot.send_message(message.chat.id, 'Введите /all, что бы узнать курсы валют на сегодня\n' '/usd - для курса доллара США\n' 
                     '/eur - для курса Евро\n' '/byn - для курса Белорусского рубля\n' '/kzt - для курса Казахстанского тенге\n'
                     '/try - для курса Турецкой лиры\n')

@bot.message_handler(commands=['all'])
def send_all(message):
    bot.send_message(message.chat.id, f'{pre_print}{all_cur}')

@bot.message_handler(commands=['usd'])
def send_usd(message):
    bot.send_message(message.chat.id, f'{pre_print}{usd_cur}')

@bot.message_handler(commands=['eur'])
def send_usd(message):
    bot.send_message(message.chat.id, f'{pre_print}{eur_cur}')

@bot.message_handler(commands=['byn'])
def send_usd(message):
    bot.send_message(message.chat.id, f'{pre_print}{byn_cur}')

@bot.message_handler(commands=['kzt'])
def send_usd(message):
    bot.send_message(message.chat.id, f'{pre_print}{kzt_cur}')

@bot.message_handler(commands=['try'])
def send_usd(message):
    bot.send_message(message.chat.id, f'{pre_print}{try_cur}')

# @bot.message_handler(func=lambda message: True)
# def handle_message(message):
#     try:
#         text = message.text.split()
#
#         if len(text) != 3:
#             raise APIException("Неправильный формат запроса! Пример: USD EUR 10")
#
#         base, quote, amount = text
#         result = CurrencyConverter.get_price(base, quote, amount)
#         bot.send_message(message.chat.id, f"Результат: {result}")
#
#     except APIException as e:
#         bot.send_message(message.chat.id, f"Ошибка: {e}")

bot.polling(none_stop=True)

