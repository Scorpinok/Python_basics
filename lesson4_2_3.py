# 2. Написать функцию currency_rates(), принимающую в качестве аргумента
# код валюты (например, USD, EUR, GBP, ...) и возвращающую курс этой валюты по отношению к рублю.
# Использовать библиотеку requests. В качестве API можно использовать
# http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация: выполнить предварительно запрос к API
# в обычном браузере, посмотреть содержимое ответа. Можно ли, используя только методы класса
# str, решить поставленную задачу? Функция должна возвращать результат числового типа,
# например float. Подумайте: есть ли смысл для работы с денежными величинами использовать
# вместо float тип Decimal? Сильно ли усложняется код функции при этом? Если в качестве
# аргумента передали код валюты, которого нет в ответе, вернуть None. Можно ли сделать работу
# функции не зависящей от того, в каком регистре был передан аргумент? В качестве примера
# выведите курсы доллара и евро.
#
# 3. *(вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса
# дату, которая передаётся в ответе сервера. Дата должна быть в виде объекта date. Подумайте,
# как извлечь дату из ответа, какой тип данных лучше использовать в ответе функции?

def currency_rates(name_currency):
    import requests
    import xml.etree.ElementTree as ET
    from datetime import datetime

    path = "http://www.cbr.ru/scripts/XML_daily.asp"

    response = requests.get(path)

    xmlDict = {}
    root = ET.fromstring(response.content)

    num_currency = len(list(root))

    count = 0
    while num_currency > count:
        if root[count][1].text == name_currency:
            print(datetime.strptime(root.attrib['Date'], '%d.%m.%Y').date())
            print(f"Курс валюты: {root[count][4].text}", name_currency)
            break
        count += 1
    else:
        print(None)


currency_rates("USD")
currency_rates("EUR")