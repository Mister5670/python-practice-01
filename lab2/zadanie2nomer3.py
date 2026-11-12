"""Запросить у пользователя 5 чисел, добавить их в список (используйте
.append() ), отсортировать его и вывести"""

import random
numbers = [random.randint(-50, 50) for _ in range(10)]
print(numbers)
print("Введите 5 чисел: ")
for i in range(5):
    numbers.append(int(input()))
print(sorted(numbers))