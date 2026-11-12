"""Посчитать сумму всех нечётных чисел от 1 до 100"""

count = 0
for i in range(1, 101):
    if i % 2 != 0:
        count += i
print(count)