"""Удалить из списка все дубликаты. С использованием множеств"""

import random
numbers = [random.randint(-50, 50) for _ in range(10)]

numbers2 = set(numbers)
print(numbers)
print(list(numbers2))