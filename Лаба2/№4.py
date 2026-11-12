str1=input('Введите элементы первого множества: ')
set1=set(str1.split())
print(sorted(set1))
str2=input('Введите элементы второго множества: ')
set2=set(str2.split())
print(sorted(set2))
print(f'Объединение {sorted(set1|set2)}')
print(f'Пересечение {sorted(set1&set2)}')

print(f'Все уникальные слова {sorted(set1-set2)} {sorted(set2-set1)}')

print('Введите первый список: ')
l1=input()
list1=list(l1.split())
print('Введите второй список: ')
l2=input()
list2=list(l2.split())
list1_set=set(list1)
list2_set=set(list2)
print(f'Общие элементы списков: {list1_set&list2_set}\n')
if list1_set <= list2_set:
    print('Первое входит во второе\n')
elif list2_set <= list1_set:
    print('Второе входит в первое\n')
else:
    print('оба разные\n')

set6=input('Введите множество: ')
set6=set(set6.split())
newset6=set()
v=int(input('Введите число для сравнения: '))
for c in set6:
    if int(c)<v:
        newset6.add(c)
print(newset6)