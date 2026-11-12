def povtor():
    while True:
        answer = input("Хотите повторить? (да/нет): ").lower().strip()
        if answer == 'да':
            return True
        if answer == 'нет':
            return False
        print("Ошибка: введите 'да' или 'нет'.")

# Задание 1. Банковский счёт

class BankAccount:
    def __init__(self, owner, number, balance=0):
        self.owner = owner
        self.number = number
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"Счёт пополнен на {amount}. Текущий баланс: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Ошибка: нельзя снять {amount}, на счёте только {self.balance}")
        else:
            self.balance = self.balance - amount
            print(f"Снято {amount}. Текущий баланс: {self.balance}")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Владелец: {self.owner}, Номер: {self.number}, Баланс: {self.balance}"


class Task1:
    def __init__(self):
        self.account1 = BankAccount("Иван", "1111-2222", 1000)
        self.account2 = BankAccount("Мария", "3333-4444", 500)

    def run(self):
        while True:
            print('\n1. Пополнить счета')
            print('2. Снять средства')
            print('3. Попробовать снять больше баланса')
            print('4. Вывести информацию о счетах')
            try:
                w = int(input('Выберите номер подзадания: '))
            except ValueError:
                print('Ошибка, введите число.')
                continue

            if w == 1:
                try:
                    a1 = int(input('Сумма пополнения счёта 1: '))
                    a2 = int(input('Сумма пополнения счёта 2: '))
                except ValueError:
                    print('Ошибка, введите число.')
                    continue
                self.account1.deposit(a1)
                self.account2.deposit(a2)
            elif w == 2:
                try:
                    a1 = int(input('Сумма снятия со счёта 1: '))
                    a2 = int(input('Сумма снятия со счёта 2: '))
                except ValueError:
                    print('Ошибка, введите число.')
                    continue
                self.account1.withdraw(a1)
                self.account2.withdraw(a2)
            elif w == 3:
                big = self.account1.get_balance() + 500
                print(f'Пытаемся снять {big} при балансе {self.account1.get_balance()}')
                self.account1.withdraw(big)
            elif w == 4:
                print(self.account1)
                print(self.account2)
            else:
                print('Ошибка: введите 1-4.')
                continue

            if not povtor():
                return

# Задание 2. Прямоугольник

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def is_square(self):
        return self.width == self.height

    def __str__(self):
        return f"Прямоугольник {self.width} x {self.height}"

    def __eq__(self, other):
        return self.get_area() == other.get_area()


class Task2:
    def __init__(self):
        self.rect1 = Rectangle(4, 5)
        self.rect2 = Rectangle(3, 3)
        self.rect3 = Rectangle(10, 2)

    def run(self):
        while True:
            print('\n1. Площадь и периметр всех прямоугольников')
            print('2. Проверить, какие из них квадраты')
            print('3. Сравнить прямоугольники по площади')
            try:
                w = int(input('Выберите номер подзадания: '))
            except ValueError:
                print('Ошибка, введите число.')
                continue

            if w == 1:
                for r in (self.rect1, self.rect2, self.rect3):
                    print(r)
                    print(f'  Площадь: {r.get_area()}, Периметр: {r.get_perimeter()}')
            elif w == 2:
                for r in (self.rect1, self.rect2, self.rect3):
                    if r.is_square():
                        print(f'{r} - квадрат')
                    else:
                        print(f'{r} - не квадрат')
            elif w == 3:
                print(f'rect1 == rect2: {self.rect1 == self.rect2}')
                print(f'rect1 == rect3: {self.rect1 == self.rect3}')
                print(f'rect2 == rect3: {self.rect2 == self.rect3}')
            else:
                print('Ошибка: введите 1-3.')
                continue

            if not povtor():
                return

# Задание 3. Животные (без подзаданий — одно действие)

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print("Какое-то животное издаёт звук")

class Dog(Animal):
    def make_sound(self):
        print("Гав!")

class Cat(Animal):
    def make_sound(self):
        print("Мяу!")

class Task3:
    def __init__(self):
        self.dog1 = Dog("Бобик", 3)
        self.dog2 = Dog("Шарик", 5)
        self.cat1 = Cat("Мурка", 2)
        self.cat2 = Cat("Барсик", 4)
        self.animals = [self.dog1, self.dog2, self.cat1, self.cat2]

    def run(self):
        print('\nВсе животные по очереди:')
        for animal in self.animals:
            animal.make_sound()
            print(f'  Имя: {animal.name}, возраст: {animal.age}')

        povtor()

# Задание 4. Товар

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        if price < 0 or quantity < 0:
            print("Ошибка: цена и количество не могут быть отрицательными")
            self.__price = 0
            self.__quantity = 0
        else:
            self.__price = price
            self.__quantity = quantity

    def add_stock(self, amount):
        if amount < 0:
            print("Ошибка: количество не может быть отрицательным")
            return
        self.__quantity = self.__quantity + amount
        print(f"Товар '{self.name}' пополнен на {amount}. На складе: {self.__quantity}")

    def sell(self, amount):
        if amount < 0:
            print("Ошибка: количество не может быть отрицательным")
            return
        if amount > self.__quantity:
            print(f"Ошибка: нельзя продать {amount}, на складе только {self.__quantity}")
        else:
            self.__quantity = self.__quantity - amount
            print(f"Продано {amount} шт. '{self.name}'. Остаток: {self.__quantity}")

    def get_total_value(self):
        return self.__price * self.__quantity

    @property
    def total_value(self):
        return self.__price * self.__quantity

class Task4:
    def __init__(self):
        self.product1 = Product("Телефон", 20000, 10)
        self.product2 = Product("Наушники", 3000, 20)

    def run(self):
        while True:
            print('\n1. Увеличить количество товара на складе')
            print('2. Продать товар')
            print('3. Попробовать продать больше, чем есть')
            print('4. Вывести общую стоимость всех товаров')
            try:
                w = int(input('Выберите номер подзадания: '))
            except ValueError:
                print('Ошибка, введите число.')
                continue

            if w == 1:
                try:
                    amount = int(input('Сколько единиц добавить товару 1? '))
                except ValueError:
                    print('Ошибка, введите число.')
                    continue
                self.product1.add_stock(amount)
            elif w == 2:
                try:
                    a1 = int(input('Сколько единиц товара 1 продать? '))
                    a2 = int(input('Сколько единиц товара 2 продать? '))
                except ValueError:
                    print('Ошибка, введите число.')
                    continue
                self.product1.sell(a1)
                self.product2.sell(a2)
            elif w == 3:
                print('Пытаемся продать 999999 единиц товара 1')
                self.product1.sell(999999)
            elif w == 4:
                print(f"Общая стоимость '{self.product1.name}': {self.product1.total_value}")
                print(f"Общая стоимость '{self.product2.name}': {self.product2.total_value}")
            else:
                print('Ошибка: введите 1-4.')
                continue

            if not povtor():
                return

# Задание 5. Время

class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}"

    def __add__(self, other):
        total_minutes = self.minutes + other.minutes
        extra_hours = total_minutes // 60
        new_minutes = total_minutes % 60
        new_hours = (self.hours + other.hours + extra_hours) % 24
        return Time(new_hours, new_minutes)

class Task5:
    def __init__(self):
        self.time1 = Time(2, 45)
        self.time2 = Time(1, 30)
        self.time3 = Time(10, 50)

    def run(self):
        while True:
            print('\n1. time1 + time2')
            print('2. time1 + time3')
            print('3. time2 + time3')
            print('4. time3 + time3')
            try:
                w = int(input('Выберите номер подзадания: '))
            except ValueError:
                print('Ошибка, введите число.')
                continue

            if w == 1:
                print(f'{self.time1} + {self.time2} = {self.time1 + self.time2}')
            elif w == 2:
                print(f'{self.time1} + {self.time3} = {self.time1 + self.time3}')
            elif w == 3:
                print(f'{self.time2} + {self.time3} = {self.time2 + self.time3}')
            elif w == 4:
                print(f'{self.time3} + {self.time3} = {self.time3 + self.time3}')
            else:
                print('Ошибка: введите 1-4.')
                continue

            if not povtor():
                return

# Главный класс

class LabWork4:
    def __init__(self):
        self.tasks = {
            1: Task1(), 2: Task2(), 3: Task3(), 4: Task4(), 5: Task5()
        }

    def run(self):
        while True:
            print('\n1. Банковский счёт')
            print('2. Прямоугольник')
            print('3. Животные')
            print('4. Товар')
            print('5. Время')
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
    LabWork4().run()