"""Вывести на экран таблицу умножения от 1 до 9 с помощью вложенных циклов"""

for i in range(1,10):
    for j in range(1,10):
        otvet = i*j
        print(i, " * ", j, " = ", otvet)