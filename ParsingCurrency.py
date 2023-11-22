from bs4 import BeautifulSoup
import requests
import time

class APIException(Exception):
    pass


# class CurrencyConverter:
#     @staticmethod
#     def get_price(base, quote, amount):
#         # Используйте API для получения курса валют
#         # Например, здесь используется бесплатное API от exchangeratesapi.io
#         url = f"https://api.exchangeratesapi.io/latest?base={base}&symbols={quote}"
#         response = requests.get(url)
#
#         if response.status_code != 200:
#             raise APIException("Ошибка получения данных")
#
#         data = response.json()
#         rate = data["rates"].get(quote)
#
#         if rate is None:
#             raise APIException("Неправильная валюта")
#
#         try:
#             amount = float(amount)
#         except ValueError:
#             raise APIException("Неправильное количество валюты")
#
#         result = rate * amount

base = 'https://www.cbr.ru/currency_base/daily/'

html = requests.get(base).content

soup = BeautifulSoup(html, 'lxml')

div = soup.find('div', class_='table')

table = div.find('table', class_='data')

rows = table.find_all('tr')
def find_currency_info(currency):
    currency_row = None
    for row in rows:
        cells = row.find_all('td')
        if len(cells) > 1 and currency in cells[1].text:
            currency_row = row
            break
    return currency_row

pre_print = ( '\n' +'Курс валют ЦБ на сегодня ' + str(time.strftime('%d.%m.%Y - %X') +'\n'))
# print('---------------------------------------')

# Находим информацию о USD
usd_row = find_currency_info('USD')
cells = usd_row.find_all('td')
usd_info = [cell.text.strip() for cell in cells]
usd_cur = (f'{usd_info[1]} - {usd_info[3]} = {usd_info[4]} рублей')
# Находим информацию о EUR
eur_row = find_currency_info('EUR')
cells = eur_row.find_all('td')
eur_info = [cell.text.strip() for cell in cells]
eur_cur = (f'{eur_info[1]} - {eur_info[3]} = {eur_info[4]} рублей')
# Находим информацию о BYN
byn_row = find_currency_info('BYN')
cells = byn_row.find_all('td')
byn_info = [cell.text.strip() for cell in cells]
byn_cur = (f'{byn_info[1]} - {byn_info[3]} = {byn_info[4]} рублей')
# Находим информацию о KZT
kzt_row = find_currency_info('KZT')
cells = kzt_row.find_all('td')
kzt_info = [cell.text.strip() for cell in cells]
kzt_cur = (f'{kzt_info[1]} - {kzt_info[3]} = {kzt_info[4]} рублей')
# Находим информацию о TRY
try_row = find_currency_info('TRY')
cells = try_row.find_all('td')
try_info = [cell.text.strip() for cell in cells]
try_cur = ('Курс валюты ' + try_info[1] + ' - ' + try_info[3] + ' = ' + try_info[4] + ' рублей')
try_cur = (f'{try_info[1]} - {try_info[3]} = {try_info[4]} рублей')

all_cur = (f"{usd_cur}\n{eur_cur}\n{byn_cur}\n{kzt_cur}\n{try_cur}")

