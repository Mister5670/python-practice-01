"""Используя срез, вывести каждый второй элемент списка, начиная с третьего
элемента"""

import random
numbers = [random.randint(-50, 50) for _ in range(10)]
numbers2 = numbers[2::2]
print(numbers)
print(numbers2)