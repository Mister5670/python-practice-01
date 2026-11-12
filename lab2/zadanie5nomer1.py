"""Сгенерировать список из 20 случайных чисел и вывести только уникальные
значения"""

import random
numbers = [random.randint(-50, 50) for _ in range(20)]

numbers2 = set(numbers)
print(numbers)
print(list(numbers2))