# Урок 3

#1.Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на
# русский язык. Например:
# >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"
# Если перевод сделать невозможно, вернуть None.

print('Задача 1\n')

def num_translate(num_name):
    num_name = num_name.lower()
    dic_num_names = { 'one': 'один','two': 'два','three': 'три',
                      'four': 'четыре', 'five': 'пять', 'six': 'шесть',
                      'seven': 'семь', 'eight': 'восемь', 'nine': 'девять',
                      'ten': 'десять', 'zero' : 'нуль', 'null' : 'ноль'
    }
    print(dic_num_names.pop(num_name, None))

num_translate("SevEn")

print('\n')

# 2. *(вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): реализовать
# корректную работу с числительными, начинающимися с заглавной буквы — результат тоже
# должен быть с заглавной. Например:
# >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"

print('Задача 2\n')

def num_translate_adv(num_name):
    dic_num_names = { 'one': 'один','two': 'два','three': 'три',
                      'four': 'четыре', 'five': 'пять', 'six': 'шесть',
                      'seven': 'семь', 'eight': 'восемь', 'nine': 'девять',
                      'ten': 'десять', 'zero' : 'нуль', 'null' : 'ноль'
    }
    if num_name.istitle():
        num_name = num_name.lower()
        return dic_num_names.pop(num_name, None).capitalize()
    else:
        num_name = num_name.lower()
        return dic_num_names.pop(num_name, None)

print(num_translate_adv("Eight"))
print(num_translate_adv("seven"))
print(num_translate_adv("nIne"))

print('\n')

# 3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и
# возвращающую словарь, в котором ключи — первые буквы имён, а значения — списки,
# содержащие имена, начинающиеся с соответствующей буквы. Например:
# >>> thesaurus("Иван", "Мария", "Петр", "Илья")
# {
# "И": ["Иван", "Илья"],
# "М": ["Мария"],
# "П": ["Петр"]
# }

print('Задача 3')

def thesaurus(*first_names):
    dict_names = dict()
    list_to_add = []
    for first_name in first_names:
        if first_name[0] not in dict_names.keys():
            dict_names[first_name[0]] = [first_name]
        else:
            list_to_add.append(first_name)
            for i in dict_names[first_name[0]]:
                list_to_add.append(i)

            dict_names[first_name[0]] = list_to_add
            list_to_add = []

    return dict_names

print(thesaurus("Иван", "Мария", "Маша", "Петр", "Илья", "Изекиль", "Иосиф"))

print('\n')

# 4. *(вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов
# строки в формате «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы
# фамилий, а значения — словари, реализованные по схеме предыдущего задания и содержащие
# записи, в которых фамилия начинается с соответствующей буквы. Например:
# >>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр
# Алексеев", "Илья Иванов", "Анна Савельева")
# {
# "А": {
# "П": ["Петр Алексеев"]
# },
# "И": {
# "И": ["Илья Иванов"]
# },
# "С": {
# "И": ["Иван Сергеев", "Инна Серова"],
# "А": ["Анна Савельева"]
# }
# }
print('Задача 4\n')

def thesaurus_adv(*first_sec_names):
    dict_second_names = dict()
    dict_first_names = dict()

    list_to_add = []

    for first_sec_name in first_sec_names:
        first_letter = first_sec_name.split(' ')[1][0]
        if first_letter not in dict_second_names.keys():
            dict_second_names[first_letter] = [first_sec_name]
        else:
            list_to_add.append(first_sec_name)

            for i in dict_second_names[first_letter]:
                list_to_add.append(i)

            dict_second_names[first_letter] = list_to_add
            list_to_add = []

    for dict_key, dict_item in dict_second_names.items():
        for first_sec_name in dict_item:
            first_letter = first_sec_name.split(' ')[0][0]
            if first_letter not in dict_first_names.keys():
                dict_first_names[first_letter] = [first_sec_name]
            else:
                list_to_add.append(first_sec_name)

                for i in dict_first_names[first_letter]:
                    list_to_add.append(i)

                dict_first_names[first_letter] = list_to_add
                list_to_add = []

        dict_second_names[dict_key] = dict_first_names
        dict_first_names = dict()

    return dict_second_names

print(thesaurus_adv("Иван Сергеев", "Иван Сергеев", "Инна Серова", "Петр Алексеев",
                    "Осетр Алексеев", "Илья Иванов", "Анна Савельева", "Ваня Савельев"))

print('\n')

# 5. # Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех
# случайных слов, взятых из трёх списков (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
# Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы
# слов в шутках (когда каждое слово можно использовать только в одной шутке)? Сможете ли вы
# сделать аргументы именованными?

print('Задача 5\n')

def get_jokes(num_joke = 1, repeat = True):
    """
    Функция get_jokes генерирует шутки случайным образом, выбирая слова из списков
    :param num_joke: количество шуток
    :param repeat: повторять слова в шутках или нет
    :return: возвращает шутку или более
    """
    import random

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    list_jokes = []

    if repeat:
        for i in range(num_joke):
            list_jokes.append(" ".join([adverbs[random.randint(0, 4)],
                                    adjectives[random.randint(0, 4)],
                                    nouns[random.randint(0, 4)]]))
    else:
        if num_joke > len(nouns):
            num_joke = 5
            print("Вы привысили возможное число шуток с неповторяющимися словами, пошучу пять раз")

        for i in range(num_joke):
            num_for_nouns = random.randint(0, len(nouns)-1)
            num_for_adverbs = random.randint(0, len(adverbs)-1)
            num_for_adjectives = random.randint(0, len(adjectives)-1)

            list_jokes.append(" ".join([adverbs[num_for_adverbs],
                                    adjectives[num_for_adjectives],
                                    nouns[num_for_nouns]]))

            adverbs.remove(adverbs[num_for_adverbs])
            adjectives.remove(adjectives[num_for_adjectives])
            nouns.remove(nouns[num_for_nouns])

    return list_jokes


print(get_jokes(num_joke=3, repeat=False))
print(help(get_jokes))

