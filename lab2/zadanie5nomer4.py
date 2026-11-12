"""Вручную создайте словарь "товар – цена" (минимум 5 пар). Найти самый
дорогой товар и вывести его название"""
slovar = {
    "мясо": 50,
    "яйца": 32,
    "огурец": 20,
    "молоко": 37,
    "рыба": 57,
    "макароны": 40
}
price = 0
nazvanie = None
for i, j in slovar.items():
    if j > price:
        price = j
        nazvanie = i
print(nazvanie, price)