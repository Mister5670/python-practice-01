"""Создать словарь, где ключи – это элементы списка, а значения – количество их
повторений"""
spisok = [1,2,3,4,5,5,4,3,2,1,10,20,30,30,20,10,7,8,9]
slovar = {}
for i in spisok:
    if i in slovar:
        slovar[i] += 1
    else:
        slovar[i] = 1

print("Словарь:")
for i, j in slovar.items():
    print(i, " - ", j)