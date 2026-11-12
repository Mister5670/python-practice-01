import random
numbers = [random.randint(-20,20) for _ in range(20)]
uniq=set(numbers)
print(sorted(numbers))
print(sorted(uniq))
print()

dict={}
for i in numbers:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(f'Словарь повторений: {dict}\n')
l=input('Введите список слов: ')
stroka=list(l.split())
len5=set()
for i in range(len(stroka)):
    if len(stroka[i])>5:
        len5.add(stroka[i])
print(len5)
print()
products = {}
print("Введите 5 товаров и их цены:")
for i in range(5):
    name = input(f"Введите название товара {i+1}: ")
    price = int(input(f"Введите цену для '{name}': "))
    products[name] = price
print("\nВаш словарь товаров:", products)
max_price = 0
best_product = ""
for product, price in products.items():
    if price > max_price:
        max_price = price
        best_product = product
print(f"\nСамый дорогой товар: {best_product} (цена: {max_price})")

user_string = input("Введите строку: ")
char_indices = {}
for index, char in enumerate(user_string):
    if char not in char_indices:
        char_indices[char] = index
print("Результат:", char_indices)