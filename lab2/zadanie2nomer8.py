"""Используя срез, развернуть список в обратном порядке"""

import random
numbers = [random.randint(-50, 50) for _ in range(10)]

numbers2 = numbers[::-1]
print(numbers)
print(numbers2)