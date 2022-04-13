# 1. Реализовать вывод информации о промежутке времени в зависимости
# от его продолжительности duration в секундах ...

print("Задание №1",end= '\n')

duration = int(input("Введите промежуток времени в секундах: "))

days = duration // 86400
hours =  (duration // 3600) - days * 24
minutes_raw =  duration - (hours + days * 24) * 3600
minutes = minutes_raw // 60
seconds = minutes_raw - minutes * 60

if days:
    print("{:02} дн {:02} час {:02} мин {:02} сек".format(days,hours,minutes,seconds))
elif hours:
    print("{:02} час {:02} мин {:02} сек".format(hours, minutes, seconds))
elif minutes:
    print("{:02} мин {:02} сек".format(minutes, seconds))
elif seconds:
    print("{:02} сек".format(seconds))

print('\n')

#2. Создать список, состоящий из кубов нечётных чисел от 1 до 1000 ...
print("Задание №2",end= '\n')

list_cubes_odds = [i**3 for i in range(1,1001,2)]
print("Список кубов нечетных чисел:",end= '\n')
print(list_cubes_odds)

list_sum_cubes = []
for i in list_cubes_odds:
    count = 0
    for x in str(i):
        count += int(x)
    if not count % 7:
        list_sum_cubes.append((i,count))
print("Список чисел и сумм чисел их составляющих, которые делятся нацело на 7:",end= '\n')
print(list_sum_cubes)

list_sum_cubes_plus = []
for i in list_cubes_odds:
    count = 0
    i += 17
    for x in str(i):
        count += int(x)
    if not count % 7:
        list_sum_cubes_plus.append((i,count))
print("Список чисел и сумм чисел их составляющих, которые делятся нацело на 7, с учетом прибавления числа 17:",end= '\n')
print(list_sum_cubes_plus)
print('\n')

#3. Реализовать склонение слова «процент» во фразе «N процентов». Вывести эту фразу на
# экран отдельной строкой для каждого из чисел в интервале от 1 до 100 ...

print("Задание №3",end= '\n')

list_for_phrase = [i for i in range(1,101)]

print("Склонение слова «процент» во фразе «N процентов»:",end= '\n')

for i in list_for_phrase:
    if i >= 11 and i <= 15 or i == 100:
        print(i,"процентов")
    elif i % 10 == 1:
        print(i, "процент")
    elif i % 10 >= 5 or i % 10 == 0:
        print(i, "процентов")
    else:
        print(i, "процента")