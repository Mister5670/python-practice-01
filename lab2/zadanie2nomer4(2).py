"""Удалить из списка все дубликаты. Без использования множеств"""

import random
numbers = [random.randint(-50, 50) for _ in range(10)]

numbers2 = []
for i in numbers:
    if i not in numbers2:
        numbers2.append(i)
print(numbers)
print(numbers2)