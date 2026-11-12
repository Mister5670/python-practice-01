"""Даны два списка. Найти общие элементы с помощью множеств"""

spisok1 = [3,6,9,12,15,18,21,24,27,30]
spisok2 = [1,2,3,4,5,6,7,8,9,10]
spisok1 = set(spisok1)
spisok2 = set(spisok2)
print(spisok1 & spisok2)