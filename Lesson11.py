# 1.Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
# строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый — с
# декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип
# к типу «Число». Второй — с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
# реальных данных.

print("Задание 1\n")

class Date:
    def __init__(self, d, m, y):
        self.d = d
        self.m = m
        self.y = y

    @classmethod
    def date_to_int(cls, d_m_y):
        if cls.valid_int(d_m_y):
            d, m, y = map(int, d_m_y.split("-"))
            return cls(d, m, y)
        else:
            return "Текст датой не является"

    @staticmethod
    def valid_int(d_m_y):
        try:
            d, m, y = map(int, d_m_y.split('-'))
            if d <= 31 and d > 0 and m <= 12 and m > 0 and y <= 9999 and y > 0:
                return True
            else:
                return False
        except Exception:
            return False

    def __str__(self):
        return f'Дата: день - {self.d}, месяц - {self.m}, год - {self.y}'


str_date = "0-0-0"
print(Date.date_to_int(str_date))

str_date = "sdf"
print(Date.date_to_int(str_date))

str_date = "09-06-2022"
print(Date.date_to_int(str_date))

print("\n")

# 2. Создать собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверить его работу на данных, вводимых пользователем. При вводе нуля в качестве
# делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

print("Задание 2\n")

class My_exception_div_err(Exception):
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val1 = val2

    def __str__(self):
        return f"Попытка деления на ноль: {val1} / {val2}"

class div_num:
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val1 = val2

    @property
    def lets_div(self):
        if val2 == 0:
            raise My_exception_div_err(val1,val2)
        else:
            return val1/val2

val1 = 1
val2 = 0

try:
    print(div_num(val1,val2).lets_div)
except Exception as err:
    print(err)

print("\n")

# 3. Создать собственный класс-исключение, который должен проверять содержимое списка на
# наличие только чисел. Проверить работу исключения на реальном примере. Запрашивать у
# пользователя данные и заполнять список необходимо только числами. Класс-исключение
# должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока
# пользователь сам не остановит работу скрипта, введя, например, команду «stop». При этом
# скрипт завершается, сформированный список с числами выводится на экран.
# Подсказка: для этого задания примем, что пользователь может вводить только числа и
# строки.
# Во время ввода пользователем очередного элемента необходимо реализовать
# проверку типа элемента. Вносить его в список, только если введено число. Класс-исключение
# должен не позволить пользователю ввести текст (не число) и отобразить соответствующее
# сообщение. При этом работа скрипта не должна завершаться.

print("Задание 3\n")

class My_exception_element_err(Exception):
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return f"{self.val} не является числом"


res_list = []
while True:
    val = input("введите число или 'stop' чтобы прекратить:")
    if val != 'stop':
        if val.isdigit():
            res_list.append(val)
        else:
            print(My_exception_element_err(val))
    else:
        print(res_list)
        break

print("\n")

# 4. Начать работу над проектом «Склад оргтехники». Создать класс, описывающий склад. А также
# класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
# конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить
# параметры, общие для приведённых типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.

# 5. Продолжить работу над предыдущим заданием. Разработать методы, которые отвечают за
# приём оргтехники на склад и передачу в определённое подразделение компании. Для
# хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру (например, словарь).

# 6. Продолжить работу над предыдущим заданием. Реализовать механизм валидации вводимых
# пользователем данных. Например, для указания количества принтеров, отправленных на
# склад, нельзя использовать строковый тип данных.

print(f"Задание 4-5-6\n")

class My_exception_warehouse_err(Exception):
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return f"Попытка ввода некорректных данных: {self.val}"

class Warehouse:
    def __init__(self):
        self._item = {}
        self._list_items = []
        self.__count = 0

    def add_new_equipment(self, obj, place, num_item):
        self.__count += 1
        self._item["№"] = self.__count
        self._item["Товар"] = str(obj)

        if str(num_item).isdigit():
             self._item["Колличество"] = num_item
        else:
            self.__count -= 1
            raise My_exception_warehouse_err(f"\n -> Колличество: {num_item} <-")

        self._item["Размещение"] = place
        self._list_items.append(self._item)
        self._item = {}

    def __str__(self):
        return '\n'.join(str(row) for row in self._list_items)

    def show_how_much(self):
        return self.__count

class Equipment:
    def __init__(self, name, prod_date, eq_type):
        self.name = name
        self.prod_date = prod_date
        self.eq_type = eq_type

class Printer(Equipment):
    def __init__(self, name, prod_date, eq_type, color=None):
        super().__init__(name, prod_date, eq_type)
        self.color = color

    def __str__(self):
        if self.color:
            pr_color = 'цветной'
        else:
            pr_color = 'ч/б'

        return f"Название: {self.name} | "  \
               f"Дата производства: {self.prod_date} | " \
               f"Тип устройства: {self.eq_type} | " \
               f"{pr_color}"

class Xerox(Equipment):
    def __init__(self, name, prod_date, eq_type, func_num=None):
        super().__init__(name, prod_date, eq_type)
        self.func_num = func_num

    def __str__(self):
        return f"Название: {self.name} | "  \
               f"Дата производства: {self.prod_date} | " \
               f"Тип устройства: {self.eq_type} | " \
               f"Количество функций: {self.func_num}"

class Scanner(Equipment):
    def __init__(self, name, prod_date, eq_type, scan_speed=None):
        super().__init__(name, prod_date, eq_type)
        self.scan_speed = scan_speed

    def __str__(self):
        return f"Название: {self.name} | "  \
               f"Дата производства: {self.prod_date} | " \
               f"Тип устройства: {self.eq_type} | " \
               f"Скорость сканирования: {self.scan_speed}"


p = Printer('hp1010', '05-12-2003', 'принтер', 1)
s = Scanner('BenQ', '07-09-2014', 'сканер', 20)
x = Xerox('Xerox100', '23-08-2011', 'ксерокс', 30)

w = Warehouse()

try:
    w.add_new_equipment(p, 'somewhere', 2)
    w.add_new_equipment(s, 'here', 2)
    w.add_new_equipment(x, 'there', -1)
except Exception as err:
    print(err)

print(f"\nВсего наименований на складе: {w.show_how_much()}")
print(f"Все что есть на складе:\n{w}")

print("\n")

# 7. Реализовать проект «Операции с комплексными числами». Создать класс «Комплексное число».
# Реализовать перегрузку методов сложения и умножения комплексных чисел. Проверить работу проекта.
# Для этого создать экземпляры класса (комплексные числа), выполнить сложение и умножение созданных экземпляров.
# Проверить корректность полученного результата.


print("Задание 7\n")


class Complex_number:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        a = self.a + other.a
        b = self.b + other.b
        return Complex_number(a, b)

    def __mul__(self, other):
        a = (self.a * other.a) - (self.b * other.b)
        b = (self.a * other.b) + (self.b * other.a)
        return Complex_number(a, b)

    def __repr__(self):
        return f'{self.a} + {self.b}i' if self.b > 0 else f'{self.a} - {abs(self.b)}i'


comp_num1 = Complex_number(23, -4)
comp_num2 = Complex_number(-5, 7)

print(f"Первое комплексное число: {comp_num1}")
print(f"Второе комплексное число: {comp_num2}")

print(f"\nИх сумма: {comp_num1 + comp_num2}")
print(f"Их произведение: {comp_num1 * comp_num2}")