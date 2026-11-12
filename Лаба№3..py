import random
from fractions import Fraction

def povtor():
    while True:
        answer = input("Хотите повторить? (да/нет): ").lower().strip()
        if answer == 'да':
            return True
        if answer == 'нет':
            return False
        print("Ошибка: введите 'да' или 'нет'.")

class Task1:

    def run(self):
        while True:
            print('\n1. Случайные числа и преобразования')
            print('2. Фильтрация слов')
            try:
                w = int(input('Выберите номер подзадания: '))
            except ValueError:
                print('Ошибка, введите число.')
                continue

            if w == 1:
                numbers = [random.randint(-100, 100) for _ in range(20)]
                print(f'Список: {numbers}')
                print(f'Квадраты: {[x ** 2 for x in numbers]}')
                print(f'Чётные: {[x for x in numbers if x % 2 == 0]}')
                print(f'Кубы нечётных: {[x ** 3 for x in numbers if x % 2 != 0]}')
                print(f'Делятся на 3 и 5: {[x for x in numbers if x % 3 == 0 and x % 5 == 0]}')
            elif w == 2:
                word = ["pyTHon", "jAva", "C++", "Rust", "Go"]
                print([x.upper() for x in word if len(x) > 3])
                print([x.lower() for x in word if len(x) == 2])
            else:
                print('Ошибка: введите 1 или 2.')
                continue

            if not povtor():
                return

class Task2:

    def __init__(self):
        self.matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    def run(self):
        while True:
            print('\n1. Одномерный список')
            print('2. Квадраты')
            print('3. Чётные')
            print('4. Диагональ')
            try:
                w = int(input('Выберите номер подзадания: '))
            except ValueError:
                print('Ошибка, введите число.')
                continue

            flat = [x for row in self.matrix for x in row]

            if w == 1:
                print(flat)
            elif w == 2:
                print([x ** 2 for x in flat])
            elif w == 3:
                print([x for x in flat if x % 2 == 0])
            elif w == 4:
                n=len(self.matrix)
                print([self.matrix[i][n-1-i] for i in range(n)])
            else:
                print('Ошибка: введите 1-4.')
                continue

            if not povtor():
                return

class FibonacciIterator:

    def __init__(self, n):
        self.n = n
        self.count = 0
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        self.count += 1
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        return result

class Task3:

    def run(self):
        while True:
            try:
                n = int(input('\nВведите количество чисел Фибоначчи n: '))
            except ValueError:
                print('Ошибка, введите число.')
                continue

            if n < 0:
                print('Ошибка: введите неотрицательное число.')
                continue

            print(f'Первые {n} чисел Фибоначчи: {list(FibonacciIterator(n))}')

            if not povtor():
                return

class PrimeGenerator:

    def __init__(self, n):
        self.n = n

    def __iter__(self):
        count, num = 0, 2
        while count < self.n:
            if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
                yield num
                count += 1
            num += 1

class Task4:

    def run(self):
        while True:
            try:
                n = int(input('\nВведите количество простых чисел n: '))
            except ValueError:
                print('Ошибка, введите число.')
                continue

            if n < 0:
                print('Ошибка: введите неотрицательное число.')
                continue

            print(f'Первые {n} простых чисел: {list(PrimeGenerator(n))}')

            if not povtor():
                return

class FractionCalculator:

    def __init__(self, s1, s2):
        self.f1 = Fraction(s1)
        self.f2 = Fraction(s2)

    def report(self):
        print(f'{self.f1} + {self.f2} = {self.f1 + self.f2}')
        print(f'{self.f1} - {self.f2} = {self.f1 - self.f2}')
        print(f'{self.f1} * {self.f2} = {self.f1 * self.f2}')
        if self.f2 == 0:
            print(f'{self.f1} / {self.f2} = деление на ноль невозможно')
        else:
            print(f'{self.f1} / {self.f2} = {self.f1 / self.f2}')

class Task5:

    def run(self):
        while True:
            try:
                s1 = input('\nВведите первую дробь (например 1/3): ').strip()
                s2 = input('Введите вторую дробь (например 2/5): ').strip()
                FractionCalculator(s1, s2).report()
            except ValueError:
                print('Ошибка: введите дробь в формате a/b или целое число.')
                continue

            if not povtor():
                return
class LabWork3:

    def __init__(self):
        self.tasks = {
            1: Task1(), 2: Task2(), 3: Task3(), 4: Task4(), 5: Task5()
        }

    def run(self):
        while True:
            print('\n1. Списковое включение')
            print('2. Обработка двумерного списка')
            print('3. Создание итератора')
            print('4. Генератор простых чисел')
            print('5. Калькулятор дробей')
            print('0. Выход')

            try:
                zad = int(input('Выберите номер задания: '))
            except ValueError:
                print('Ошибка, введите ЧИСЛО.')
                continue

            if zad == 0:
                print('Работа программы завершена.')
                break

            task = self.tasks.get(zad)
            if task is None:
                print('Ошибка: нет такого задания.')
                continue

            task.run()

if __name__ == '__main__':
    LabWork3().run()