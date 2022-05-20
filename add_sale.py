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

bakery_path = "bakery.csv"

if not os.path.isfile(bakery_path):
    with open(bakery_path, mode='w', encoding='UTF-8'):
        pass

if len(argv) == 2:
    value_to_file = argv[1]
else:
    raise SystemExit(1)

with open(bakery_path, mode='r', encoding='UTF-8') as bakery_f:
    bakery_count = sum(1 for row in bakery_f)

with open(bakery_path, mode='a', encoding='UTF-8') as bakery_f:
    bakery_count += 1
    bakery_f.write(f'{bakery_count}\t{value_to_file}\n')