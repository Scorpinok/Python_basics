# 1. Не используя библиотеки для парсинга, распарсить (получить определённые данные)
# файл логов web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) — получить
# список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
#
# [
# ...
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('173.255.199.22', 'GET', '/downloads/product_2'),
# ...
# ]
#
# Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.

print('Задача 1\n')

import requests
import os

file_link = "https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs"
from_requests = requests.get(file_link).content

with open('from_requests.txt', 'w') as f:
    f.write(from_requests.decode('UTF-8'))

if (os.path.isfile("res_file.txt")):
    os.remove("res_file.txt")

from_user = input('Если хотите записать файл введите "y": ')

if from_user != 'y':
    res_list = []

with open('from_requests.txt', 'rb') as f:
    for item in f:
        file_element = item.split()

        set_to_file = (str(file_element[0]).replace("b",'').replace("'",''),
                         str(file_element[5]).replace("b",'').replace("'",'').replace('"',''),
                         str(file_element[6]).replace("b",'').replace("'",''))

        if from_user == 'y':
            with open('res_file.txt', 'a') as res_f:
                res_f.write(f"{str(set_to_file)}\n")
        else:
            res_list.append(set_to_file)

if from_user != 'y':
    print(f"Результирующиый список:\n{res_list}")

print('\n')


# 2. * (вместо 1) Найти IP адрес спамера и количество отправленных им запросов по
# данным файла логов из предыдущего задания.
# Примечания: спамер — это клиент, отправивший больше всех запросов;
# код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.

print('Задача 2\n')

import requests

file_link = "https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs"
from_requests = requests.get(file_link).content

with open('from_requests.txt', 'w') as f:
    f.write(from_requests.decode('UTF-8'))

with open('from_requests.txt', 'rb') as f:
    dict_ip = {}
    max_el, ip, dict_el = 0, 0, 0
    for item in f:
        file_element = item.split()

        str_to_file = str(file_element[0]).replace("b",'').replace("'",'')

        dict_el = dict_ip[str_to_file] + 1 if str_to_file in dict_ip else 1
        if dict_el > max_el:
            max_el, ip = dict_el, str_to_file
        dict_ip[str_to_file] = dict_el

print(f"IP адрес спамера:\n{ip} и его число запросов {max_el}")

print('\n')

# 3. Есть два файла: в одном хранятся ФИО пользователей сайта,
# а в другом — данные об их хобби. Известно, что при хранении
# данных используется принцип: одна строка — один пользователь,
# разделитель между значениями — запятая. Написать код, загружающий
# данные из обоих файлов и формирующий из них словарь: ключи — ФИО,
# значения — данные о хобби. Сохранить словарь в файл.
# Проверить сохранённые данные. Если в файле, хранящем данные
# о хобби, меньше записей, чем в файле с ФИО, задаём в словаре
# значение None. Если наоборот — выходим из скрипта с кодом «1».
# При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.

# Фрагмент файла с данными о пользователях (users.csv):
# Иванов,Иван,Иванович
# Петров,Петр,Петрович
# Фрагмент файла с данными о хобби (hobby.csv):
# скалолазание,охота,горные лыжи

# 4. * (вместо 3) Решить задачу 3 для ситуации, когда объём данных
# в файлах превышает объём ОЗУ (разумеется, не нужно реально создавать
# такие большие файлы, это просто задел на будущее проекта). Также реализовать
# парсинг данных из файлов — получить отдельно фамилию, имя и отчество для
# пользователей и название каждого хобби: преобразовать в какой-нибудь контейнерный тип
# (список, кортеж, множество, словарь). Обосновать выбор типа. Подумать, какие могут
# возникнуть проблемы при парсинге. В словаре должны храниться данные, полученные
# в результате парсинга.

# 5. ** (вместо 4) Решить задачу 4 и реализовать интерфейс командной строки,
# чтобы можно было задать путь к обоим исходным файлам и путь к выходному файлу
# со словарём. Проверить работу скрипта для случая, когда все файлы находятся в разных папках.

print('Задача 3-4-5\n')

import csv
import json
import os

import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.lift()
root.attributes("-topmost", True)
root.withdraw()

# user_to_file =  "Иванов,Иван,Иванович\n"
# hobby_to_file = "скалолазание,охота,горные лыжи\nпрогулки,рыбалка,прыжки\n"

user_to_file = "Иванов,Иван,Иванович\nПетров,Петр,Петрович\n"
hobby_to_file = "скалолазание,охота,горные лыжи\n"

with open('user_file.csv', 'w', encoding='UTF-8') as res_f:
    res_f.write(user_to_file)

with open('hobby_file.csv', 'w', encoding='UTF-8') as res_f:
    res_f.write(hobby_to_file)

user_path = filedialog.askopenfilename(initialdir=os.getcwd(),
                                       title="Select USER file",
                                       filetypes=(("CSV files", "user_file.csv"),
                                                  ("JSON files", "*.json"),
                                                  ("All files", "*.*")))

hobby_path = filedialog.askopenfilename(initialdir=os.getcwd(),
                                       title="Select HOBBY file",
                                       filetypes=(("CSV files", "hobby_file.csv"),
                                                  ("JSON files", "*.json"),
                                                  ("All files", "*.*")))

with open(user_path, mode='r', encoding='UTF-8') as user_f:
    user_count = sum(1 for row in user_f)
with open(hobby_path, mode='r', encoding='UTF-8') as hobby_f:
    hobby_count = sum(1 for row in hobby_f)

if user_count < hobby_count:
    raise SystemExit(1)
else:
    with open(hobby_path, mode='a', encoding='UTF-8') as hobby_f:
        for i in range(user_count - 1):
            hobby_f.write('None\n')

dict_res = {}
with open(user_path, mode='r', encoding='UTF-8') as user_f:
    with open(hobby_path, mode='r', encoding='UTF-8') as hobby_f:
        for i, user_line in enumerate(csv.reader(user_f)):
            for hobby_line in csv.reader(hobby_f):
                if len(hobby_line) != 1:
                    dict_res[f"{user_line[0]} {user_line[1]} {user_line[2]}"] = f"{hobby_line[0]}, {hobby_line[1]}, {hobby_line[2]}"
                else:
                    dict_res[f"{user_line[0]} {user_line[1]} {user_line[2]}"] = f"{hobby_line[0]}"
                break

with open('user_hobby_file.json', 'w', encoding='UTF-8') as res_f:
    json.dump(dict_res, res_f)

json_string = json.dumps(dict_res, indent=4, ensure_ascii=False)
print(f'Содержимое json файла: \n {json_string}')

with open('user_hobby_file.json', 'r', encoding='UTF-8') as res_f:
    print(f"Считали файл json:\n{json.load(res_f)}")

print('\n')
