"""Поменять местами первый и последний элемент списка"""

import random
numbers = [random.randint(-50, 50) for _ in range(10)]
print(numbers)
pervoeold = numbers[0]
posledneeold = numbers[-1]
numbers[0] = posledneeold
numbers[-1] = pervoeold
print(numbers)