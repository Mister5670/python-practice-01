"""Сгенерировать последовательность Фибоначчи длиной n и вывести её"""

n = int(input("Введите число: "))
spisok = []
pervoe = 0
vtoroe = 1
for i in range(n):
    spisok.append(pervoe)
    pervoeold = pervoe
    pervoe = vtoroe
    vtoroe = vtoroe + pervoeold
print(spisok)