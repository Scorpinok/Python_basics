# 6. Реализовать простую систему хранения данных о суммах продаж булочной.
# Должно быть два скрипта с интерфейсом командной строки: для записи
# данных и для вывода на экран записанных данных. При записи передавать
# из командной строки значение суммы продаж. Для чтения данных реализовать
# в командной строке следующую логику:

# просто запуск скрипта — выводить все записи;

# запуск скрипта с одним параметром-числом — выводить все записи с номера,
# равного этому числу, до конца;

# запуск скрипта с двумя числами — выводить записи, начиная с номера,
# равного первому числу, по номер, равный второму числу, включительно.

# Подумать, как избежать чтения всего файла при реализации второго и третьего случаев.
# Данные хранить в файле bakery.csv в кодировке utf-8. Нумерация
# записей начинается с 1. Примеры запуска скриптов:
#
# python add_sale.py 5978,5
# python add_sale.py 8914,3
# python add_sale.py 7879,1
# python add_sale.py 1573,7
# python show_sales.py
# 5978,5
# 8914,3
# 7879,1
# 1573,7
# python show_sales.py 3
# 7879,1
# 1573,7
# python show_sales.py 1 3
# 5978,5
# 8914,3
# 7879,1

from sys import  argv
import os

bakery_path = 'bakery.csv'

if not os.path.isfile(bakery_path):
    raise SystemExit(1)

if len(argv) == 3:
    value_to_show_start = argv[1]
    value_to_show_end = argv[2]

elif len(argv) == 2:
    value_to_show_start = argv[1]
    value_to_show_end = ''
else:
    value_to_show_start = ''
    value_to_show_end = ''

if value_to_show_start and not value_to_show_end:
    with open(bakery_path, mode='r', encoding='UTF-8') as bakery_f:
        for i, item in enumerate(bakery_f):
            if i >= int(value_to_show_start) - 1:
                print(item.replace('\n', '').split('\t')[1])

elif not value_to_show_start and value_to_show_end:
    with open(bakery_path, mode='r', encoding='UTF-8') as bakery_f:
        for i, item in enumerate(bakery_f):
            if i >= int(value_to_show_end) - 1:
                print(item.replace('\n','').split('\t')[1])

elif value_to_show_start and value_to_show_end:
    if int(value_to_show_start) < int(value_to_show_end):
        with open(bakery_path, mode='r', encoding='UTF-8') as bakery_f:
            for i, item in enumerate(bakery_f):
                if i >= int(value_to_show_start) - 1:
                    print(item.replace('\n', '').split('\t')[1])
                    if i == int(value_to_show_end) - 1:
                        break
    else:
        with open(bakery_path, mode='r', encoding='UTF-8') as bakery_f:
            for i, item in enumerate(bakery_f):
                if i >= int(value_to_show_end) - 1:
                    print(item.replace('\n', '').split('\t')[1])
                    if i == int(value_to_show_start) - 1:
                        break

elif not value_to_show_start and not value_to_show_end:
    with open(bakery_path, mode='r', encoding='UTF-8') as bakery_f:
        for item in bakery_f:
            print(item.replace('\n', '').split('\t')[1])