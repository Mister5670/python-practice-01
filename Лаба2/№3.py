journal={'Вадим':4,'Вася':5,'Никита':4,'Алексей':3,'Женя':3}
g=journal.values()
print(f'Средний балл: {sum(g)/len(g)}')

str = input('Введите строку: ').lower()
letter_count = {}
for char in str:
    if char.isalpha():
        letter_count[char] = letter_count.get(char, 0) + 1
print(letter_count)

kvadrat={}
for i in range(11):
    kvadrat[i] = i**2
print(kvadrat)
print()

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
dic = {}
for i in range(len(list1)):
    dic[list1[i]] = list2[i]
print(dic)