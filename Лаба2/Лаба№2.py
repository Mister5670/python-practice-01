def zad1():
    print('1: Вывести на экран таблицу умножения от 1 до 9 с помощью вложенных циклов.')
    print('2: Посчитать сумму всех нечётных чисел от 1 до 100')
    print('3: Запросить у пользователя число n и вывести все его делители')
    print('4: Найти факториал числа, введённого пользователем, с помощью цикла')
    print('5: Сгенерировать последовательность Фибоначчи длиной n и вывести её')
    print('Выберите номер подзадания: ')
    while True:
        try:
            w=int(input())
            if w<1 or w>5:
                print('Введите в диапазоне номеров заданий: ')
                continue
            if w == 1:
                for i in range(1, 10):
                    for c in range(1, 11):
                        print(f'{i} x {c} = {i * c}')
                    print()

            elif w == 2:
                a = 0
                for i in range(1, 101):
                    if i % 2 != 0:
                        a += i
                print(a)

            elif w == 3:
                n = int(input('Введите число: '))
                i=1
                while i<=n:
                    if n%i==0:
                        print(f'Делитель для {n}: {i} ')
                    i += 1
            elif w == 4:

                x = int(input('Введите число для факториала: '))
                if x < 0:
                    print("Факториал не определён для отрицательных чисел")
                else:
                    c = 1
                    for i in range(2, x + 1):
                        c *= i
                    print(f'Факториал числа: {c}')

            elif w == 5:

                y = int(input('Введите число для последовательности Фибоначчи: '))
                if y <= 0:
                    print('Число должно быть больше 0')
                elif y == 1:
                    print([0])
                elif y == 2:
                    print([0, 1])
                else:
                    fib = [0, 1]
                    for i in range(2, y):
                        fib.append(fib[i - 1] + fib[i - 2])
                    print(fib)

        except ValueError:
            print('Ошибка, введите ЧИСЛО: ')
            continue
        while True:
            answer = input("Хотите выполнить ещё один подпункт? (да/нет): ").lower().strip()
            if answer == 'да':
                print('Выберите номер подзадания: ')
                break
            elif answer == 'нет':
                print("Работа программы завершена.")
                return
            else:
                print("Ошибка: пожалуйста, введите 'да' или 'нет'.")

def zad2():
    print('1: Создать список из 10 чисел и вывести только чётные элементы.')
    print('2: Найти максимальное и минимальное число в списке.')
    print('3: Запросить у пользователя 5 чисел, добавить их в список (используйте.append() ), отсортировать его и вывести.')
    print('4: Удалить из списка все дубликаты. Реализовать два варианта: со множествами и без них.')
    print('5: Поменять местами первый и последний элемент списка.')
    print('6: Используя срез, вывести каждый второй элемент списка, начиная с третьего элемента.')
    print('7: Используя срезы, разделить список на две равные части и вывести обе части. Если количество элементов нечётное, то первая часть должна содержать на один элемент больше (реализовать с помощью if - else ).')
    print('8: Используя срез, развернуть список в обратном порядке')
    print('9: С помощью среза вывести последние 3 элемента списка')
    print('Выберите номер подзадания: ')
    import random
    numbers = [random.randint(-50, 50) for _ in range(10)]
    while True:
        try:
            w = int(input())
            if w<1 or w>9:
                print('Введите в диапазоне номеров заданий: ')
                continue
            if w == 1:
                print(numbers)
                import random
                print('Четные элементы: ')
                for i in range(len(numbers)):
                    if numbers[i] % 2 == 0:
                        print(numbers[i])

            elif w == 2:
                print(f'Максимальное число: {max(numbers)}')
                print(f'Минимальное число: {min(numbers)}')

            elif w == 3:
                sorted_numbers = sorted(numbers)
                print('Введите 5 чисел:')
                for _ in range(5):
                    c = int(input())
                    sorted_numbers.append(c)
                print(sorted(sorted_numbers))

            elif w == 4:
                print('Без дубликатов 1) : ')
                print(sorted(set(numbers)), '\n')
                print(('Без дубликатов 2) : '))
                uniq = []
                for num in numbers:
                    if num not in uniq:
                        uniq.append(num)
                uniq = sorted(uniq)
                print(uniq)
                print()
                x = uniq[0]
                uniq[0] = uniq[len(uniq) - 1]
                uniq[len(uniq) - 1] = x

            elif w == 5:
                sorted_numbers = sorted(numbers)
                sorted_numbers[0],sorted_numbers[len(sorted_numbers)-1]=sorted_numbers[len(sorted_numbers)-1],sorted_numbers[0]
                print(f'Поменянные местами: {sorted_numbers[0]} и {sorted_numbers[len(numbers) - 1]}\n')
                print(sorted_numbers)

            elif w == 6:
                sorted_numbers = sorted(numbers)
                print(sorted_numbers)
                print('Список начиная с 3 элемента с шагом 2: ')
                print(sorted_numbers[2::2])

            elif w == 7:
                sorted_numbers = sorted(numbers)
                if len(sorted_numbers) % 2 == 0:
                    first_half = sorted_numbers[:len(sorted_numbers) // 2]
                    second_half = sorted_numbers[len(sorted_numbers) // 2:]
                else:
                    first_half = sorted_numbers[:len(sorted_numbers) // 2 + 1]
                    second_half = sorted_numbers[len(sorted_numbers) // 2 + 1:]
                print(f'Первая часть: {first_half}')
                print(f'Вторая часть: {second_half}')

            elif w == 8:
                sorted_numbers = sorted(numbers)
                print(f'В обратном порядке: {sorted_numbers[::-1]} \n')

            elif w == 9:
                sorted_numbers = sorted(numbers)
                print(sorted_numbers)
                print(f'Первые 3 элемента: {sorted_numbers[0:3]}')
        except ValueError:
            print('Ошибка, введите ЧИСЛО: ')
            continue
        while True:
            answer = input("Хотите выполнить ещё один подпункт? (да/нет): ").lower().strip()
            if answer == 'да':
                print('Выберите номер подзадания: ')
                break
            if answer == 'нет':
                print("Работа программы завершена.")
                return
            else:
                print("Ошибка: пожалуйста, введите 'да' или 'нет'.")
def zad3():
    print('1: Создать словарь с именами студентов и их оценками, вывести средний балл.')
    print('2: Подсчитать количество каждой буквы в строке (словарь: буква → количество). Пользователь сначала с помощью input() вводит строку, затем программа создает необходимый словарь.')
    print('3: Создать словарь, где ключи – это числа от 1 до 10, а значения – их квадраты.')
    print('4: Составить словарь из двух списков: список ключей и список значений.')
    print('Выберите номер подзадания: ')
    while True:
        try:
            w=int(input())
            if w<1 or w>4:
                print('Введите в диапазоне номеров заданий: ')
                continue
            if w == 1:
                journal = {'Вадим': 4, 'Вася': 5, 'Никита': 4, 'Алексей': 3, 'Женя': 3}
                g = journal.values()
                print(f'Средний балл: {sum(g) / len(g)}')

            elif w == 2:
                str = input('Введите строку: ').lower()
                letter_count = {}
                for char in str:
                    if char.isalpha():
                        letter_count[char] = letter_count.get(char, 0) + 1
                print(letter_count)

            elif w == 3:
                kvadrat = {}
                for i in range(1,11):
                    kvadrat[i] = i ** 2
                print(kvadrat)

            elif w == 4:
                list1 = [1, 2, 3, 4, 5]
                list2 = [6, 7, 8, 9, 10]
                dic = {}
                for i in range(len(list1)):
                    dic[list1[i]] = list2[i]
                print(dic)
        except ValueError:
            print('Ошибка, введите ЧИСЛО: ')
            continue
        while True:
            answer = input("Хотите выполнить ещё один подпункт? (да/нет): ").lower().strip()
            if answer == 'да':
                print('Выберите номер подзадания: ')
                break
            if answer == 'нет':
                print("Работа программы завершена.")
                return
            else:
                print("Ошибка: пожалуйста, введите 'да' или 'нет'.")
def zad4():
    print('1: Создать два множества и вывести их пересечение и объединение.')
    print(
        '2: Найти все уникальные слова в тексте, введённом пользователем.')
    print('3: Даны два списка. Найти общие элементы с помощью множеств.')
    print('4: Проверить, является ли одно множество подмножеством другого.')
    print('5: Удалить из множества все элементы, которые меньше заданного числа.')
    print('Выберите номер подзадания: ')
    while True:
        try:
            w=int(input())
            if w<1 or w>5:
                print('Введите в диапазоне номеров заданий: ')
                continue

            if w == 1:
                str1 = input('Введите элементы первого множества: ')
                set1 = set(str1.split())
                print(sorted(set1))
                str2 = input('Введите элементы второго множества: ')
                set2 = set(str2.split())
                print(sorted(set2))
                print(f'Объединение {sorted(set1 | set2)}')
                print(f'Пересечение {sorted(set1 & set2)}')


            elif w == 2:
                text = input('Введите текст: ').lower()
                words = text.split()
                counts = {}
                for word in words:
                    counts[word] = counts.get(word, 0) + 1
                unique_once = [word for word, count in counts.items() if count == 1]
                print('Слова, которые встречаются ровно один раз:')
                print(unique_once)

            elif w == 3:
                print('Введите первый список: ')
                l1 = input()
                list1 = list(l1.split())
                print('Введите второй список: ')
                l2 = input()
                list2 = list(l2.split())
                list1_set = set(list1)
                list2_set = set(list2)
                print(f'Общие элементы списков: {list1_set & list2_set}\n')

            elif w == 4:
                if list1_set <= list2_set:
                    print('Первое входит во второе\n')
                elif list2_set <= list1_set:
                    print('Второе входит в первое\n')
                else:
                        print('оба разные\n')

            elif w == 5:
                set6 = input('Введите множество: ')
                set6 = set(set6.split())
                newset6 = set()
                v = int(input('Введите число для сравнения: '))
                for c in set6:
                    if int(c) >= v:
                        newset6.add(c)
                print(newset6)
        except ValueError:
            print('Ошибка, введите ЧИСЛО: ')
            continue
        while True:
            answer = input("Хотите выполнить ещё один подпункт? (да/нет): ").lower().strip()
            if answer == 'да':
                print('Выберите номер подзадания: ')
                break
            if answer == 'нет':
                print("Работа программы завершена.")
                return
            else:
                print("Ошибка: пожалуйста, введите 'да' или 'нет'.")
def zad5():
    print('1: Сгенерировать список из 20 случайных чисел и вывести только уникальные значения.')
    print(
        '2: Создать словарь, где ключи – это элементы списка, а значения – количество их повторений.')
    print('3: Дан список слов. Создать множество из слов, длина которых больше 5 символов.')
    print('4: Вручную создайте словарь "товар – цена" (минимум 5 пар). Найти самый дорогой товар и вывести его название.')
    print('5: Запросить у пользователя строку и составить словарь: символ → индекс его первого вхождения.')
    print('Выберите номер подзадания: ')
    while True:
        import random
        numbers = [random.randint(-20, 20) for _ in range(20)]
        try:
            w=int(input())
            if w<1 or w>5:
                print('Введите в диапазоне номеров заданий: ')
                continue
            if w == 1:
                uniq = set(numbers)
                print(sorted(numbers))
                print(sorted(uniq))
                print()

            elif w == 2:
                dict = {}
                for i in numbers:
                    if i in dict:
                        dict[i] += 1
                    else:
                        dict[i] = 1
                print(f'Словарь повторений: {dict}\n')

            elif w == 3:
                l = input('Введите список слов: ')
                stroka = list(l.split())
                len5 = set()
                for i in range(len(stroka)):
                    if len(stroka[i]) > 5:
                        len5.add(stroka[i])
                print(len5)

            elif w == 4:
                products = {'телефон': 500, 'ноутбук': 500}
                #print("Введите 5 товаров и их цены:")
               #for i in range(5):
                  #  name = input(f"Введите название товара {i + 1}: ")
                   # price = int(input(f"Введите цену для '{name}': "))
                    #products[name] = price
               # print("\nВаш словарь товаров:", products)
                max_price = 0
                best_product = []
                for product, price in products.items():
                    if price > max_price or price==max_price:
                        max_price = price
                        best_product.append(product)

                print(f"\nСамый дорогой товар: {best_product} (цена: {max_price})")

            elif w == 5:
                user_string = input("Введите строку: ")
                char_indices = {}
                for index, char in enumerate(user_string):
                    if char not in char_indices:
                        char_indices[char] = index
                print("Результат:", char_indices)
        except ValueError:
            print('Ошибка, введите ЧИСЛО: ')
            continue
        while True:
            answer = input("Хотите выполнить ещё один подпункт? (да/нет): ").lower().strip()
            if answer == 'да':
                print('Выберите номер подзадания: ')
                break
            if answer == 'нет':
                print("Работа программы завершена.")
                return
            else:
                print("Ошибка: пожалуйста, введите 'да' или 'нет'.")
print('Задание №1: Циклы')
print('Задание №2: Списки')
print('Задание №3: Словари')
print('Задание №4: Множества')
print('Задание №5: Комбинированные задания')
while True:
    try:
        print('Выберите номер основного задания:')
        zad = int(input())
        if zad>5 or zad<1:
            print('Ошибка, введите в диапазоне заданий: ')
            continue
    except ValueError:
        print('Ошибка, введите число: ')
        continue
    if zad == 1:
        zad1()
    if zad == 2:
        zad2()
    if zad == 3:
        zad3()
    if zad == 4:
        zad4()
    if zad == 5:
        zad5()