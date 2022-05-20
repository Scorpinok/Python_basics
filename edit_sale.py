
# 7. * (вместо 6) Добавить возможность редактирования данных при помощи
# отдельного скрипта: передаём ему номер записи и новое значение. При этом
# файл не должен читаться целиком — обязательное требование. Предусмотреть
# ситуацию, когда пользователь вводит номер записи, которой не существует.

from sys import  argv
import os
import shutil

bakery_path = "bakery.csv"

if not os.path.isfile(bakery_path):
    raise SystemExit(1)

if len(argv) == 3:
    num_value_to_file = argv[1]
    value_to_file = argv[2]
else:
    raise SystemExit(1)

bakery_path_temp = "bakery_temp.csv"
shutil.copy(bakery_path, bakery_path_temp)

with open(bakery_path_temp, mode='r', encoding='UTF-8') as bakery_from_f:
    with open(bakery_path, mode='w', encoding='UTF-8') as bakery_to_f:
        for i, item in enumerate(bakery_from_f):
            if i == int(num_value_to_file) - 1:
                bakery_to_f.write(f"{i + 1}\t{value_to_file}\n")
            else:
                bakery_to_f.write(f"{item}")

if (os.path.isfile(bakery_path_temp)):
    os.remove(bakery_path_temp)