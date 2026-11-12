"""Составить словарь из двух списков: список ключей и список значений"""

keys = ["Иванов", "Петров", "Андреев", "Сергеев", "Романов"]
values = [3, 5, 4, 5, 3]
slovar = {}
for i in range(len(keys)):
    slovar[keys[i]] = values[i]
print(slovar)