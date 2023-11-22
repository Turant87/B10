import requests
import json
import lxml.html
from lxml import etree

# r = requests.get('https://baconipsum.com/api/?type=all-meat&paras=3&start-with-lorem=1&format=html')
# print(r.content)
# print(r.status_code)

# r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')
# texts = json.loads(r.content)
# print(type(texts))
# for text in texts:
#     print(text[:50], '\n')

# s = requests.get('https://api.github.com')
# d = json.loads(s.content)
# print(type(s))
# print(d['following_url'])
# print(s.content)
# print(r.content)
# print(r.status_code)

# r = requests.post('https://httpbin.org/post', data = {'key':'value'}) # отправляем пост запрос
# print(r.content) # содержимое ответа и его обработка происходит также как и с ГЕТ запросами, разницы никакой нету

# data = {'key': 'value'}
# r = requests.post('https://httpbin.org/post', json=json.dumps(data))
# print(r.content)

# r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')
# r = json.loads(r.content)
# print(r[0])

# html = requests.get('https://www.python.org/').content
# tree = lxml.html.document_fromstring(html)
# title = tree.xpath('/html/head/title/text()')
#
# print(title)

#
# # создадим объект ElementTree. Он возвращается функцией parse()
# tree = etree.parse('Welcome to Python.org.html', lxml.html.HTMLParser())  # попытаемся спарсить наш файл с помощью html парсера. Сам html - это то что мы скачали и поместили в папку из браузера.
#
# # date = tree.findall('//*[@id="content"]/div/section/div[3]/div[1]/div/ul/li/time')
# ul = tree.findall('//*[@id="content"]/div/section/div[3]/div[1]/div/ul/li')  # помещаем в аргумент методу findall скопированный xpath. Здесь мы получим все элементы списка новостей. (Все заголовки и их даты)
# # создаём цикл в котором мы будем выводить название каждого элемента из списка
# for li in ul:
#     a = li.find('a')  # в каждом элементе находим где хранится заголовок новости. У нас это тег <a>. Т.е. гиперссылка на которую нужно нажать, чтобы перейти на страницу с новостью. (Гиперссылки в html это всегда тэг <a>)
#     date_time = li.find('time')
#     print(date_time.get('datetime'), a.text)  # из этого тега забираем текст - это и будет нашим названием

# import redis
#
# red = redis.Redis(
#     host='127.0.0.1',
#     port=6379,
#     password=''
# )
#
# red.set('var1', 'value1')  # записываем в кеш строку "value1"
# print(red.get('var1'))  # считываем из кеша данные
#
# import redis
# import \
#     json  # так так так, кто это тут у нас? Наш старый друг Джейсон заглянул на огонёк! Ну привет, чем ты сегодня нас порадуешь?
#
# red = redis.Redis(
#     host='127.0.0.1',
#     port=6379,
#     password=''
# )
#
# dict1 = {'key1': 'value1', 'key2': 'value2'}  # создаём словарь для записи
# red.set('dict1', json.dumps(dict1))  # с помощью функции dumps() из модуля json превратим наш словарь в строчку
# converted_dict = json.loads(
#     red.get('dict1'))  # с помощью знакомой нам функции прерващаем данные полученные из кеша обратно в словарь
# print(type(converted_dict))  # убеждаемся что мы получили действительно словарь
# print(converted_dict)  # ну и выводим его содержание

import redis
import json

red = redis.Redis(
    host='127.0.0.1',
    port=6379,
password =''
)

cont = True

while cont:
    action = input('action:\t')
    if action == 'write':
        name = input('name:\t')
        phone = input('phone:\t')
        red.set(name, phone)
    elif action == 'read':
        name = input('name:\t')
        phone = red.get(name)
        if phone:
            print(f'{name}\'s phone is {str(phone)}')
    elif action == 'delete':
        name = input('name:\t')
        phone = red.delete(name)
        if phone:
            print(f"{name}'s phone is deleted")
        else:
            print(f"Not found {name}")
    elif action == 'stop':
        break
