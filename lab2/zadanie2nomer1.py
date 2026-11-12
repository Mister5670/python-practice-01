""" Создать список из 10 чисел и вывести только чётные элементы"""

import random
numbers = [random.randint(-50, 50) for _ in range(10)]

spisok = []
for i in numbers:
    if i % 2 == 0:
        spisok.append(i)
print(numbers)
print(spisok)