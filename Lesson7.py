# 1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp

print('Задача 1\n')

import os

start_dir = os.getcwd()
dir_name = f'{start_dir}/my_project_task1'
sub_dir_names = ["settings", "mainapp", "adminapp", "authapp"]

try:

    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
        for item in sub_dir_names:
            if not os.path.exists(f"{dir_name}/{item}"):
                os.mkdir(f"{dir_name}/{item}")
    else:
        for item in sub_dir_names:
            if not os.path.exists(f"{dir_name}/{item}"):
                os.mkdir(f"{dir_name}/{item}")

except Exception as e:
    print("Возникла ошибка", e)
else:
    print("Папки созданы!")

print('\n')

# 2. * (вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
# |--my_project
#    |--settings
#    |  |--__init__.py
#    |  |--dev.py
#    |  |--prod.py
#    |--mainapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--mainapp
#    |        |--base.html
#    |        |--index.html
#    |--authapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--authapp
#    |        |--base.html
#    |        |--index.html

print('Задача 2\n')

import yaml

yml = """
my_project:
-settings: __init__.py, dev.py, prod.py
-mainapp: __init__.py, models.py, views.py
--templates:
---mainapp: base.html, index.html
-authapp: __init__.py, models.py, views.py
--templates:
---authapp: base.html, index.html
"""

try:

    with open('config.yaml', 'w') as f:
        yaml.safe_dump(yml, f)

    with open('config.yaml') as f:
        data_from_f = yaml.safe_load(f)

    start_dir = os.getcwd()
    data_from_f = data_from_f.split('\n')

    for i in data_from_f:
        if i:
            dir_name = i.split(':')
            if dir_name[0].find('-') == -1:
                first_dir = f'{start_dir}/{dir_name[0]}'
                if not os.path.exists(first_dir):
                    os.mkdir(first_dir)
            elif dir_name[0].find('--') == -1:
                sec_dir = f'{first_dir}/{dir_name[0].replace("-","")}'
                if not os.path.exists(sec_dir):
                    os.mkdir(sec_dir)
                files_names = dir_name[1].split(',')
                for el in files_names:
                    file_name = f"{sec_dir}/{el.strip()}"
                    with open(file_name,'w'):
                        pass
            elif dir_name[0].find('---') == -1:
                third_dir = f'{sec_dir}/{dir_name[0].replace("--","")}'
                if not os.path.exists(third_dir):
                    os.mkdir(third_dir)
            else:
                forth_dir = f'{third_dir}/{dir_name[0].replace("---","")}'
                if not os.path.exists(forth_dir):
                    os.mkdir(forth_dir)
                files_names = dir_name[1].split(',')
                for el in files_names:
                    file_name = f"{forth_dir}/{el.strip()}"
                    with open(file_name,'w'):
                        pass

except Exception as e:
    print("Возникла ошибка", e)
else:
    print("Папки созданы!")

print('\n')

# 3. Создать структуру файлов и папок, как написано в задании 2
# (при помощи скрипта или «руками» в проводнике). Написать скрипт,
# который собирает все шаблоны в одну папку templates, например:
# |--my_project
#    ...
#   |--templates
#    |   |--mainapp
#    |   |  |--base.html
#    |   |  |--index.html
#    |   |--authapp
#    |      |--base.html
#    |      |--index.html
# Примечание: исходные файлы необходимо оставить;
# обратите внимание, что html-файлы расположены в родительских папках
# (они играют роль пространств имён); предусмотреть возможные исключительные
# ситуации; это реальная задача, которая решена, например, во фреймворке django.

print('Задача 3\n')

import shutil
import os

start_dir = os.getcwd()
proj_name = 'my_project'
work_dir = f'{start_dir}/{proj_name}'

folder_name = "templates"
new_templates = f"{work_dir}/{folder_name}"
if not os.path.exists(new_templates):
    os.mkdir(new_templates)

try:

    for root, dirs, files in os.walk(work_dir):
        if root.find('templates') != -1 and files:
            for el in files:
                file_to_copy = f"{root}/{el}"
                check_file = f"{folder_for_templates}/{el}"
                if not os.path.exists(check_file):
                    shutil.copy(file_to_copy, folder_for_templates)
        elif root.find('templates') != -1 and not files:
            if len(dirs) > 0:
                folder_for_templates = f"{new_templates}/{dirs[0]}"
                if not os.path.exists(folder_for_templates):
                    os.mkdir(folder_for_templates)

except Exception as e:
    print("Возникла ошибка", e)
else:
    print("Файлы скопированы!")

print('\n')

# 4. Написать скрипт, который выводит статистику для заданной папки в виде словаря,
# в котором ключи — верхняя граница размера файла (пусть будет кратна 10),
# а значения — общее количество файлов (в том числе и в подпапках), размер
# которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
#     {
#       100: 15,
#       1000: 3,
#       10000: 7,
#       100000: 2
#     }
# Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
# Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.
# 5. * (вместо 4) Написать скрипт, который выводит статистику для заданной папки
# в виде словаря, в котором ключи те же, а значения — кортежи вида (<files_quantity>,
# [<files_extensions_list>]), например:
#   {
#       100: (15, ['txt']),
#       1000: (3, ['py', 'txt']),
#       10000: (7, ['html', 'css']),
#       100000: (2, ['png', 'jpg'])
#     }
# Сохраните результаты в файл <folder_name>_summary.json в той же папке,
# где запустили скрипт.

print('Задача 4-5\n')

import os
import json

root_dir = os.getcwd()

max_el = 0
def get_max_file_size(work_dir, max_el):

    for dir in os.listdir(work_dir):
        abs_path = os.path.join(work_dir, dir)

        if os.path.isdir(abs_path):
            get_max_file_size(abs_path, max_el)
        else:
            if os.stat(abs_path).st_size >= max_el:
                max_el = os.stat(abs_path).st_size
                with open("max_file_size.txt", 'w') as f:
                    f.write(str(max_el))

get_max_file_size(root_dir, max_el)

with open("max_file_size.txt", 'r') as f:
    max_el = f.read()

max_el = int(max_el)

def walk_by_folders(work_dir):

    for dir in os.listdir(work_dir):
        abs_path = os.path.join(work_dir, dir)

        if os.path.isdir(abs_path):
            walk_by_folders(abs_path)
        else:
            with open("file_list.txt", 'a') as f:
                f.write(f"{abs_path}\n")

walk_by_folders(root_dir)

num_class = 5
files_dict = {}

file_size_step = round(max_el / num_class)
file_size_step = round(((int(str(file_size_step)[0]) + 1) * 10 ** len(str(file_size_step))) / 10)

max_el = file_size_step * num_class

file_size_step_min = 0
file_size_step_max = file_size_step

while file_size_step_max <= max_el:
    count = 0
    ext_list = []
    with open("file_list.txt", 'r') as f:
        for item in f:
            item = item.replace('\n','')
            if os.stat(item).st_size < file_size_step_max and os.stat(item).st_size >= file_size_step_min:
                count += 1
                _, file_extension = os.path.splitext(item)
                ext_list.append(file_extension)
                files_dict[file_size_step_max] = (count, list(set(ext_list)))

    file_size_step_min += file_size_step
    file_size_step_max += file_size_step

print(f"Статистика по каталогу {root_dir}:\n{files_dict}")

with open('folder_stat.json', 'w', encoding='UTF-8') as res_f:
    json.dump(files_dict, res_f)

json_string = json.dumps(files_dict, indent=4, ensure_ascii=False)
print(f'\nСодержимое json файла:\n{json_string}')

with open('folder_stat.json', 'r', encoding='UTF-8') as res_f:
    print(f"Считали файл json:\n{json.load(res_f)}")

if (os.path.isfile("file_list.txt")):
    os.remove("file_list.txt")

if (os.path.isfile("max_file_size.txt")):
    os.remove("max_file_size.txt")