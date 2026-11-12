import random
from fractions import Fraction
def zad1():
    while True:
        print('1. Используя библиотеку random создайте список из 20 случайных целых числа,'
              'находящихся в диапазоне от -100 до 100 включительно.')
        print('2. Дан список, состоящий из строк: word = ["python", "java", "c++", "rust","go"]')
        try:
            w=int(input('Выберите номер подзадания:'))
            if w <1 or w>2:
                print('Ошибка, введите число в диапазоне заданий: ')
                continue
            elif w==1:
                print('Далее, на основе полученного случайного списка сформируйте:'
                  'Список квадратов всех чисел;'
                  'Список только чётных чисел;'
                  'Список кубов нечётных чисел;'
                  'Список чисел, которые делятся одновременно на 3 и 5.')
                numbers = [random.randint(-100, 100) for _ in range(20)]
                sqw=[x**2 for x in numbers]
                chet=[x for x in numbers if x%2==0]
                cube=[x**3 for x in numbers if x%2!=0]
                ThreeFive=[x for x in numbers if x%3==0 and x%5==0]
                print(numbers)
                print(f'Список квадратов всех чисел: {sqw}')
                print(f'Список только чётных чисел: {chet}')
                print(f'Список кубов нечётных чисел: {cube}')
                print(f'Список чисел, которые делятся одновременно на 3 и 5: {ThreeFive}')

            elif w==2:
                print('Создайте новый список, который содержит только слова длиннее 3'
                      'символов. Также новый список должен привести все слова к '
                      'верхнему регистру.')
                word = ["python", "java", "c++", "rust", "go"]
                new_word=[x.upper() for x in word if len(x)>3]
                print(new_word)
        except ValueError:
            print('Ошибка, введите число: ')
            continue
        if not povtor():
            return

def zad2():
    while True:
        print('Дан список: matrix = ['
              '[1, 2, 3],'
              '[4, 5, 6],'
              '[7, 8, 9]]')
        print('1. Получите одномерный список всех элементов матрицы;')
        print('2. Получите список квадратов всех элементов;')
        print('3. Получите список только чётных элементов;')
        print('4. Получите диагональ матрицы.')
        try:
            w=int(input('Выберите номер подзадания:'))
            matrix = [
                      [1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]
            ]
            q = [q for x in matrix for q in x]
            if w <1 or w>4:
                print('Ошибка, введите число в диапазоне заданий: ')
                continue
            elif w==1:
                print(f'одномерный список всех элементов матрицы: {q}')
            elif w==2:
                sqw=[t**2 for t in q]
                print(f'список квадратов всех элементов: {sqw}')
            elif w==3:
                chet = [t for t in q if t % 2 == 0]
                print(f'список только чётных элементов: {chet}')
            elif w==4:
                diag=[x[i] for i, x in enumerate(matrix)]
                print(f'диагональ матрицы: {diag}')
        except ValueError:
            print('Ошибка, введите число: ')
            continue
        if not povtor():
            return


class FibonacciIterator:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        self.count += 1
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        return result

def zad3():
    while True:
        print('Создайте собственный итератор FibonacciIterator, который последовательно'
              ' возвращает первые n чисел последовательности Фибоначчи.')
        print('Класс должен реализовывать методы: __init__(n), __iter__(), __next__().'
              ' После выдачи n чисел итератор должен вызвать исключение StopIteration.')
        try:
            n = int(input('Введите количество чисел Фибоначчи n: '))
            if n < 0:
                print('Ошибка, введите неотрицательное число: ')
                continue
            fib = FibonacciIterator(n)
            result = [number for number in fib]
            print(f'Первые {n} чисел Фибоначчи: {result}')
        except ValueError:
            print('Ошибка, введите число: ')
            continue
        if not povtor():
            return

def prime_numbers(n):
    count = 0
    num = 2
    while count < n:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
            count += 1
        num += 1

def zad4():
    while True:
        print('Создайте генератор prime_numbers(n), который возвращает первые n простых чисел.')
        print('Например: list(prime_numbers(10)) должно вернуть: '
              '[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]')
        try:
            n = int(input('Введите количество простых чисел n: '))
            if n < 0:
                print('Ошибка, введите неотрицательное число: ')
                continue
            result = list(prime_numbers(n))
            print(f'Первые {n} простых чисел: {result}')
        except ValueError:
            print('Ошибка, введите число: ')
            continue
        if not povtor():
            return

def zad5():
    while True:
        print('Введите две рациональные дроби, например: 1/3 и 2/5.')
        print('Программа вычислит сумму, разность, произведение и частное,'
              ' результат автоматически сокращается (используется тип Fraction).')
        try:
            s1 = input('Введите первую дробь (например 1/3): ').strip()
            s2 = input('Введите вторую дробь (например 2/5): ').strip()
            f1 = Fraction(s1)
            f2 = Fraction(s2)
            print(f'{f1} + {f2} = {f1 + f2}')
            print(f'{f1} - {f2} = {f1 - f2}')
            print(f'{f1} * {f2} = {f1 * f2}')
            if f2 == 0:
                print(f'{f1} / {f2} = деление на ноль невозможно')
            else:
                print(f'{f1} / {f2} = {f1 / f2}')
        except ValueError:
            print('Ошибка, введите дробь в формате a/b или целое число: ')
            continue
        if not povtor():
            return

def povtor():
    while True:
        answer = input("Хотите повторить? (да/нет): ").lower().strip()
        if answer == 'да':
            print('Выберите номер подзадания: ')
            return True
        elif answer == 'нет':
            print("Работа программы завершена.")
            return False
        else:
            print("Ошибка: пожалуйста, введите 'да' или 'нет'.")

while True:
    try:
        print('1. Списковое включение (List Comprehension)')
        print('2. Обработка двумерного списка')
        print('3. Создание итератора')
        print('4. Генератор простых чисел')
        print('5. Калькулятор дробей')
        print('Выберите номер основного задания:')
        zad = int(input())
        if zad>5 or zad<1:
            print('Ошибка, введите в диапазоне заданий: ')
            continue
    except ValueError:
        print('Ошибка, введите ЧИСЛО')
        continue
    if zad == 1:
        zad1()
    if zad == 2:
        zad2()
    if zad == 3:
        zad3()
    if zad == 4:
        zad4()
    if zad == 5:
        zad5()