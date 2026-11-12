""" Найти максимальное и минимальное число в списке"""

import random
numbers = [random.randint(-50, 50) for _ in range(10)]
print(numbers)
print("Максимальное: ",max(numbers))
print("Минимальное: ",min(numbers))