# 1. Написать функцию email_parse(<email_address>), которая при помощи
# регулярного выражения извлекает имя пользователя и почтовый домен из
# email адреса и возвращает их в виде словаря. Если адрес не валиден,
# выбросить исключение ValueError. Пример:

# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   ...
#     raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru

print('Задача 1\n')

RE_MAIL = r'(\w+[-=+]?\w+)@([A-z]+[-+]?[a-z]\.\w+)'

str_to_split_1 = 'some-ones678780@geek_brains.ru'
str_to_split_2 = 'sdgfe=sb99@gbrains.ru'
str_to_split_3 = 'sdgfesb19-876@dghd.ru'
str_to_split_4 = 'sdgfesb19_877gfrthrt@dghd.ae.com'
str_to_split_5 = 'sdgfesb19_875@gfrthrt@d.gh'

def email_parse(re_str, str_to_check):
    import re

    reg_val = re.compile(re_str)
    res_list = reg_val.split(str_to_check)

    if reg_val.match(str_to_check):
        resdict = {}
        resdict["username"] = res_list[1]
        resdict["domain"] = res_list[2]
        if res_list[3]:
            resdict["domain"] = f'{res_list[2]}{res_list[3]}'
        return resdict

    else:
        raise ValueError(f'wrong email {str_to_check}')


print(email_parse(RE_MAIL, str_to_split_1))
print(email_parse(RE_MAIL, str_to_split_2))
print(email_parse(RE_MAIL, str_to_split_3))
print(email_parse(RE_MAIL, str_to_split_4))

# для проверки на исключительную ситуацию
#print(email_parse(RE_MAIL, str_to_split_5))

print('\n')

# 2. * (вместо 1) Написать регулярное выражение для парсинга файла логов
# web-сервера из ДЗ 6 урока nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
# для получения информации вида: (<remote_addr>, <request_datetime>, <request_type>,
# <requested_resource>, <response_code>, <response_size>), например:
#
# raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2
# HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'
# parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')

print('Задача 2\n')

import re
import requests
import os

reg_val = re.compile(r'(([0-9]{1,3}[\.]){3}[0-9]{1,3}|\w+) - - \[([0-9]*/[Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec]*?/[0-9]*:\w+:\w+:\w+[ ][-+]?\w+)] \"(\w+) (/\w+/\w+) \w+/\w+\.\w+\" (\w+) (\w+) ')


file_link = "https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs"
from_requests = requests.get(file_link).content

with open('from_requests.txt', 'w') as f:
    f.write(from_requests.decode('UTF-8'))

from_user = input('Если хотите записать файл введите "y": ')

if from_user != 'y':
    res_list = []
else:
    if (os.path.isfile("res_file.txt")):
        os.remove("res_file.txt")

with open('from_requests.txt', 'rb') as f:
    for item in f:

        file_element = reg_val.split(str(item).replace("b",''))

        set_to_file = (file_element[1],file_element[3],
                       file_element[4],file_element[5],
                       file_element[6],file_element[7])

        if from_user == 'y':
            with open('res_file.txt', 'a') as res_f:
                res_f.write(f"{str(set_to_file)}\n")
        else:
            res_list.append(set_to_file)

if from_user != 'y':
    print(f"Результирующий список:\n{res_list}")

print('Обработка завершена\n')
print('\n')

# 3. Написать декоратор для логирования типов позиционных аргументов функции, например:
# def type_logger...
#     ...
#
#
# @type_logger
# def calc_cube(x):
#    return x ** 3
#
# >>> a = calc_cube(5)
# 5: <class 'int'>
# Примечание: если аргументов несколько - выводить данные о каждом через запятую;
# можете ли вы вывести тип значения функции? Сможете ли решить задачу для именованных
# аргументов? Сможете ли вы замаскировать работу декоратора? Сможете ли вывести
# имя функции, например, в виде:
# >>> a = calc_cube(5)
# calc_cube(5: <class 'int'>)

print('Задача 3\n')

def type_logger(func):
    def type_val(*args,**kwargs):
        type_list = []

        if args:
            for el in args:
                type_list.append(f'({el}, {type(el)})')
            return type_list

        if kwargs:
            for el in kwargs.values():
                type_list.append(f'({el}, {type(el)})')
            return type_list

    return type_val


@type_logger
def calc_power(x,y):
   return x ** y


print(calc_power(x=5,y=7))
print(calc_power(2,3))


@type_logger
def calc_square(x):
   return x ** 2

print(calc_square(x=5))
print(calc_square(2))

print('\n')

# 4. Написать декоратор с аргументом-функцией (callback), позволяющий
# валидировать входные значения функции и выбрасывать исключение ValueError,
# если что-то не так, например:
# def val_checker...
#     ...
#
#
# @val_checker(lambda x: x > 0)
# def calc_cube(x):
#    return x ** 3
#
#
# >>> a = calc_cube(5)
# 125
# >>> a = calc_cube(-5)
# Traceback (most recent call last):
#   ...
#     raise ValueError(msg)
# ValueError: wrong val -5

print('Задача 4\n')

def val_checker(func):
    def decorator(f):
        def new_f(*args, **kwargs):
            if args:
                if func(args[0]) == False:
                    raise ValueError(f"wrong value {args[0]}")
                else:
                    return f(args[0])

            if kwargs:
                for el in kwargs.values():
                    if func(el) == False:
                        raise ValueError(f"wrong value {el}")
                    else:
                        return f(el)
        return new_f
    return decorator


@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3


print(calc_cube(x=4))
print(calc_cube(5))
print(calc_cube(-7))

