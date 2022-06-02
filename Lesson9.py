# 1. Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд,
# второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.

print(f"\nЗадание 1")

import time

class TrafficLight:

    def __init__(self, x):
        self.x = x
        self.__color = ['\033[41m    \033[0;0m', 7,
                       '\033[43m    \033[0;0m', 2,
                       '\033[42m    \033[0;0m', 4,
                       '\033[43m    \033[0;0m', 2]

    def running(self):
        print(f'Работает светофор\n'
              f'он меняет свои состояния:')

        while self.x:
            for i in range(0, len(self.__color) - 1, 2):
                if i == 0:
                    print(f"{self.__color[i]} \033[40m    \033[0;0m \033[40m    \033[0;0m", end='')

                if i == 2:
                    print(f"\033[40m    \033[0;0m {self.__color[i]} \033[40m    \033[0;0m", end='')

                if i == 4:
                    print(f"\033[40m    \033[0;0m \033[40m    \033[0;0m {self.__color[i]}", end='')

                if i == 6:
                    if self.x == 1:
                        break

                    print(f"\033[40m    \033[0;0m {self.__color[i]} \033[40m    \033[0;0m", end='')

                time.sleep(self.__color[i + 1])
                print(f"\r", end='')

            self.x -= 1
        else:
            print(f"\033[40m    \033[0;0m \033[40m    \033[0;0m \033[40m    \033[0;0m")
            print('Работа светофора закончена!')


x = int(input('Укажите количество циклов работы светофора:'))
Tr_obj = TrafficLight(x)
Tr_obj.running()

# 2. Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина * ширина * масса асфальта для покрытия одного кв. метра
# дороги асфальтом, толщиной в 1 см * число см толщины полотна;
# проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.

print(f"\nЗадание 2")

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def count_mass(self):
        try:
            print(f"С учетом ваших параметров, вам нужно: "
                  f"{round((int(self._length) * int(self._width) * 25 * 5) / 1000)} т асфальта")
        except Exception as err:
            print(str(err))


r_obj = Road(input("Введите длину дороги (м):"), input("Введите ширину дороги (м):"))
r_obj.count_mass()

# 3. Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени
# сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса
# Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.

print(f"\nЗадание 3")

class Worker:
    def __init__(self, name, surname, position, income, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {}
        self._income["wage"] = income
        self._income["bonus"] = bonus


class Position(Worker):

    def get_full_name(self):
        print(f"Полное имя сотрудника: {self.name} {self.surname}")

    def get_total_income(self):
        try:
            print(f"Доход сотрудника: {int(self._income['wage']) + int(self._income['bonus'])}")
        except Exception as err:
            print(str(err))


name = input('Введите имя сотрудника:')
surname = input('Введите фамилию сотрудника:')
position = input('Введите должность сотрудника:')
wage = input('Введите зарплату сотрудника:')
bonus = input('Введите премию сотрудника:')

w_obj = Position(name, surname, position, wage, bonus)

w_obj.get_full_name()
w_obj.get_total_income()

# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты:
# speed, color, name, is_police(булево).
# А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.

print(f"\nЗадание 4")

import random

class Car:
    def __init__(self, speed, solor, name, is_police):
        self.speed = speed
        self.color = solor
        self.name = name
        self.is_police = is_police

    def go(self):
        if int(self.speed) > 0:
            print(f'Машина едет')

    def stop(self):
        if int(self.speed) == 0:
            print(f'Машина остановилась')

    def turn_to_direction(self):
        if int(self.speed) > 0:
            x = random.randint(0, 100)
            if x > 30:
                print(f'Машина повернула направо')
            elif x > 30 and x < 60:
                print(f'Машина повернула налево')
            else:
                print(f'Машина не стала поварачивать')
        else:
            print(f'Машина стоит, как же она может куда-то повернуть?')

    def showspeed(self):
        print(f'Скорость машины:  {self.speed} км/ч')


class TownCar(Car):
    def showspeed(self):
        if int(self.speed) <= 60:
            print(f'Скорость машины: {self.speed} км/ч')
        else:
            print(f'Скорость машины: Превышена! {self.speed} км/ч')


class SportCar(Car):
    def speed_increase(self,speed):
        self.speed += 10


class WorkCar(Car):
    def showspeed(self):
        if int(self.speed) <= 40:
            print(f'Скорость машины: {self.speed} км/ч')
        else:
            print(f'Скорость машины: Превышена! {self.speed} км/ч')


class PoliceCar(Car):
    def is_light(self,speed):
        if speed > 60:
            print(f'Мигалки включены, погоня началась!')


speed = input('Введите скорость машины:')
color = input('Введите цвет машины:')
name = input('Введите название машины:')
c_obj = Car(speed, color, name, True)

speed = input('Введите скорость городской машины:')
tc_obj = TownCar(speed, 'Черный', 'VAZ', False)

speed = input('Введите скорость машины для работы:')
wc_obj = WorkCar(speed, 'Оранжевый', 'GAZ', False)

pc_obj = PoliceCar(60, 'Оранжевый', 'Police', True)
sc_obj = SportCar(200, 'Синий', 'ferrari', False)

print(f"\nСкорость Спорткара: {sc_obj.speed}")
pc_obj.is_light(sc_obj.speed)
sc_obj.speed_increase(sc_obj.speed)
sc_obj.speed_increase(sc_obj.speed)
sc_obj.speed_increase(sc_obj.speed)
print(f"Спорткар прибавил скорость {sc_obj.speed}")

print(f"\nПоказать скорость:")
c_obj.showspeed()
tc_obj.showspeed()
wc_obj.showspeed()
pc_obj.showspeed()

print(f"\nМетоды ехать, повернуть, остановиться:")
print(f"Машина {sc_obj.name}, ее цвет  {sc_obj.color}")
sc_obj.go()
sc_obj.turn_to_direction()
sc_obj.stop()

print(f"Машина {tc_obj.name}, ее цвет  {tc_obj.color}")
tc_obj.go()
tc_obj.turn_to_direction()
tc_obj.stop()

print(f"\nЯвляется ли машина полицией:")
if tc_obj.is_police != True:
    print(f"Машина {tc_obj.name}, ее цвет  {tc_obj.color}")
    print(f'{tc_obj.name} это не полиция')

if pc_obj.is_police == True:
    print(f'{pc_obj.name} это полиция')

# 5. Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw.
# Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный
# метод для каждого экземпляра.

print(f"\nЗадание 5")

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки: {self.title}')


class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки ручкой: {list(self.title)}')


class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки карандашом: {self.title * 3}')


class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки маркером: {self.title + self.title}')


s_obj = Stationery(input("\nВведите любое слово: "))
p_obj = Pen(input("Введите любое слово: "))
pncl_obj = Pencil(input("Введите любое слово: "))
h_obj = Handle(input("Введите любое слово: "))
print("\n")

s_obj.draw()
p_obj.draw()
pncl_obj.draw()
h_obj.draw()
