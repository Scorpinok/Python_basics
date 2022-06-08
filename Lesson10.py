# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
# (метод __init__()), который должен принимать данные (список списков)
# для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода __str__() для
# вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для сложения
# двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно.
# Первый элемент первой строки первой матрицы складываем с первым
# элементом первой строки второй матрицы и пр.

print("Задание 1\n")

import random

class Matrix:
    def __init__(self, data):
        self.data = data

    def gen_matrix(num_el_row, num_el_col, limit_el):
        """
        Метод генерирует матрицу указанного размера
        :param num_el_row: количество строк
        :param num_el_col: количество столбцов
        :param limit_el: правая граница случайных значений
        :return: матрица указанного размера
        """
        result = []
        numbers = []
        for i in range(0, num_el_row):
            for j in range(0, num_el_col):
                numbers.append(random.randint(0, limit_el))
                if len(numbers) == num_el_col:
                    result.append(numbers)
                    numbers = []
        return result

    def __str__(self):
        return '\n'.join(' '.join(map(str, row)) for row in self.data)

    def __add__(self, other):
        result = []
        numbers = []

        row_count_a = len(self.data)
        col_count_a = len(self.data[0])

        row_count_b = len(other.data)
        col_count_b = len(other.data[0])

        if row_count_a == row_count_b and col_count_a == col_count_b:
            for i in range(0, row_count_a):
                for j in range(0, col_count_b):
                    numbers.append(self.data[i][j] + other.data[i][j])
                    if len(numbers) == col_count_b:
                        result.append(numbers)
                        numbers = []
        else:
            raise ValueError(f"Матрицы разного размера: "
                             f"{row_count_a}x{col_count_a} & {row_count_b}x{col_count_b}")

        return Matrix(result)


a = Matrix(Matrix.gen_matrix(3,3,100))
b = Matrix(Matrix.gen_matrix(3,3,100))

print(f'Матрица 1:\n{a}')
print(f'Матрица 2:\n{b}')
print(f'Сумма матриц:\n{a + b}')

print("\n")

# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь
# определённое название. К типам одежды в этом проекте относятся пальто и
# костюм. У этих типов одежды существуют параметры: размер (для пальто) и
# рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма(2*H + 0.3). Проверить работу этих
# методов на реальных данных.
# Выполнить общий подсчёт расхода ткани. Проверить на практике полученные
# на этом уроке знания. Реализовать абстрактные классы для основных классов
# проекта и проверить работу декоратора @property.

print("Задание 2\n")

from abc import ABC, abstractmethod

class Dress(ABC):
    @abstractmethod
    def square_count(self):
        pass

class Coat(Dress):
    def __init__(self, v):
        self.v = v

    def square_count(self):
        return f'{float(self.v) / 6.5 + 0.5:.2f}'

    @property
    def getparam(self):
        return float(self.square_count())


class Suit(Dress):
    def __init__(self, h):
        self.h = h

    def square_count(self):
        return f"{2 * float(self.h) + 0.3:.2f}"

    @property
    def getparam(self):
        return float(self.square_count())

try:
    c = Coat(input("Введите размер для пальто: "))
    s = Suit(input("Введите рост для костюма: "))

    print(f'\nДля пальто необходимо -> {str(c.square_count())} <- ткани')
    print(f'Для костюма необходимо -> {str(s.square_count())} <- ткани')

    print(f"\nСуммарный расход ткани: {c.getparam + s.getparam:.2f}")

except Exception as err:
    print(err)

print("\n")

# 3. Осуществить программу работы с органическими клетками, состоящими из ячеек.
# Необходимо создать класс «Клетка». В его конструкторе инициализировать параметр,
# соответствующий количеству ячеек клетки (целое число). В классе должны быть реализованы
# методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()),
# умножение (__mul__()), деление (__floordiv__, __truediv__()).
# Эти методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
# умножение и округление до целого числа деления клеток, соответственно.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно
# равняться сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять, только если
# разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создаётся общая клетка из двух. Число ячеек общей клетки — произведение
# количества ячеек этих двух клеток.
# Деление. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как
# целочисленное деление количества ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и
# количество ячеек в ряду. Этот метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек
# между \n равно переданному аргументу. Если ячеек на формирование ряда не хватает,
# то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, а количество ячеек в ряду — 5.
# В этом случае метод make_order() вернёт строку: *****\n*****\n**.
# Или, количество ячеек клетки — 15, а количество ячеек в ряду равняется 5.
# Тогда метод make_order() вернёт строку: *****\n*****\n*****.

print("Задание 3\n")

import random

class Cell:
    def __init__(self, cell_num):
        self.cell_num = cell_num

    def __add__(self, other):
        x = self.cell_num + other.cell_num
        return x if x > 0 else "Клетки закончились!"

    def __sub__(self, other):
        x = self.cell_num - other.cell_num
        return x if x > 0 else "Клетки закончились!"

    def __mul__(self, other):
        x = self.cell_num * other.cell_num
        return x if x > 0 else "Клетки закончились!"

    def __truediv__(self, other):
        if other.cell_num > 0:
            x = round(self.cell_num / other.cell_num)
            return x if x >= 1 else "Клетки закончились!"
        else:
            raise ValueError(f"Деление на ноль!")

    def __floordiv__(self, other):
        if other.cell_num > 0:
            x = self.cell_num // other.cell_num
            return x if x >= 1 else "Клетки закончились!"
        else:
            raise ValueError(f"Деление на ноль!")

    @property
    def make_order(self):
        x = ''
        num_el = round(self.cell_num ** 0.5)

        num_to_min = self.cell_num - num_el ** 2

        for i in range(0, num_el):
            if i == num_el - 1 and num_to_min < 0:
                val = self.cell_num - num_el * abs(num_to_min) - num_el
                if val < num_el:
                    x += ('*' * val + "\n")
                else:
                    x += ('*' * (self.cell_num - num_el * (num_el - 1)) + "\n")
            else:
                x += ('*' * num_el) + "\n"
        else:
            if num_to_min > 0:
                x += ('*' * num_to_min) + "\n"
        return x


cells_group_one = Cell(random.randint(0, 100))
print(f'Группа клеток 1: {str(cells_group_one.cell_num)}')
print(f"\n{cells_group_one.make_order}")

cells_group_two = Cell(random.randint(0, 100))
print(f'Группа клеток 2: {str(cells_group_two.cell_num)}')
print(f"\n{cells_group_two.make_order}")

x = cells_group_one + cells_group_two
print(f'Стало ячеек (+): {str(x)}')

x = cells_group_one - cells_group_two
print(f'Стало ячеек (-): {str(x)}')

x = cells_group_one * cells_group_two
print(f'Стало ячеек (*): {str(x)}')

x = cells_group_one / cells_group_two
print(f'Стало ячеек (/): {str(x)}')

x = cells_group_one // cells_group_two
print(f'Стало ячеек (//): {str(x)}')
