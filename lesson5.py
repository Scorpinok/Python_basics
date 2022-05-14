# 1. Написать генератор нечётных чисел от 1 до n (включительно),
# используя ключевое слово yield, например:
# >>> odd_to_15 = odd_nums(15)
# >>> next(odd_to_15)
# 1
# >>> next(odd_to_15)
# 3
# ...
# >>> next(odd_to_15)
# 15
# >>> next(odd_to_15)
# ...StopIteration...

print('Задача 1\n')

def odd_nums(num):
    for i in range(1, num + 1):
        yield i
    yield "Вывели все числа"

odd_to_num = odd_nums(3)

print(next(odd_to_num))
print(next(odd_to_num))
print(next(odd_to_num))
print(next(odd_to_num))

print('\n')

# 2. * (вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно),
# не используя ключевое слово yield.
print('Задача 2\n')

def odd_nums_gen(num):
    return (i for i in range(1, num + 1))

odd_to_num = odd_nums_gen(3)

try:
    print(next(odd_to_num))
    print(next(odd_to_num))
    print(next(odd_to_num))
    print(next(odd_to_num))
except StopIteration:
    print("Вывели все числа")

print('\n')

# 3. Есть два списка:
# tutors = [
#     'Иван', 'Анастасия', 'Петр', 'Сергей',
#     'Дмитрий', 'Борис', 'Елена'
# ]
# klasses = [
#     '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
# ]
# Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:
# ('Иван', '9А')
# ('Анастасия', '7В')
# ...
# Количество генерируемых кортежей не должно быть больше длины списка tutors.
# Если в списке klasses меньше элементов, чем в списке tutors, необходимо вывести
# последние кортежи в виде: (<tutor>, None), например:
# ('Станислав', None)

### Доказать, что вы создали именно генератор. Проверить его работу вплоть до истощения.

print('Задача 3\n')

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
#klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
klasses = ['9А', '7В', '9Б', '9В', '8Б']

def lists_concat(tutors, klasses):
    if len(klasses) < len(tutors):
        num_el_to_put = len(tutors) - len(klasses)
        while num_el_to_put > 0:
            klasses.append(None)
            num_el_to_put -= 1

    return (i for i in zip(tutors, klasses))

odd_to_num = lists_concat(tutors, klasses)

try:
    print(next(odd_to_num))
    print(next(odd_to_num))
    print(next(odd_to_num))
    print(next(odd_to_num))
    print(next(odd_to_num))
    print(next(odd_to_num))
    print(next(odd_to_num))
    print(next(odd_to_num))

except StopIteration:
    print("Вывели все элементы")

print('\n')

### 4. Представлен список чисел. Необходимо вывести те его элементы,
# значения которых больше предыдущего, например:
# src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [12, 44, 4, 10, 78, 123]

#src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

print('Задача 4\n')

import random
src = [random.randint(1, 100) for _ in range(10)]
print(f'Список src:\n{src}')

result = [x for i, x in enumerate(src) if i-1 >= 0 and x > src[i-1]]
print(f'Список result:\n{result}')

print('\n')

# 5. Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.
# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать из этих элементов список с сохранением порядка их следования
# в исходном списке, например:
# src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]

print('Задача 5\n')

src = [random.randint(1, 10) for _ in range(10)]
print(f'Список src:\n{src}')

set_for_result = set()
result = [x for x in src if x not in set_for_result and not set_for_result.add(x)]
print(f'Список result:\n{result}')


