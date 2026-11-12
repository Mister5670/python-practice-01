"""Подсчитать количество каждой буквы в строке (словарь: буква → количество).
Пользователь сначала с помощью input() вводит строку, затем программа
создает необходимый словарь"""

line = str(input())
slovar = {}
for i in line:
    if i in slovar:
        slovar[i] += 1
    else:
        slovar[i] = 1
print("Словарь:")
for i, j in slovar.items():
    print(i," - ", j)