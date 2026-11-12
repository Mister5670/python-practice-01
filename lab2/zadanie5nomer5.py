"""Запросить у пользователя строку и составить словарь: символ → индекс его
первого вхождения"""

text = str(input("Введите строку: "))
slovar = {}
for i in range(len(text)):
    symbol = text[i]
    if symbol not in slovar:
        slovar[symbol] = i

print("Словарь:")
for i, j in slovar.items():
    print(i, " - ", j)