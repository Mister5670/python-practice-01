""" Используя срезы, разделить список на две равные части и вывести обе части.
Если количество элементов нечётное, то первая часть должна содержать на
один элемент больше (реализовать с помощью if - else )"""

import random
numbers = [random.randint(-50, 50) for _ in range(10)]

if len(numbers) % 2 == 0:
    seredina = len(numbers) // 2
else:
    seredina = len(numbers) // 2 + 1
first = numbers[:seredina:]
second = numbers[seredina::]

print(numbers)
print(first)
print(second)