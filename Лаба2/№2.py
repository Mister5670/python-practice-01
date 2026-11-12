import random
numbers = [random.randint(-50, 50) for _ in range(10)]
print(f'Случайный список из 10 чисел: {numbers}')
print('Четные элементы: ')
for i in range(len(numbers)):
    if numbers[i]%2==0:
        print(numbers[i])
print()

print(f'Максимальное число: {max(numbers)}')
print(f'Минимальное число: {min(numbers)}')
print()

print('Введите 5 чисел:')
for _ in range(5):
    c=int(input())
    numbers.append(c)
print(sorted(numbers))

print('Без дубликатов 1) : ')
print(sorted(set(numbers)),'\n')
print(('Без дубликатов 2) : '))
uniq=[]
for num in numbers:
    if num not in uniq:
        uniq.append(num)
uniq = sorted(uniq)
print(uniq)
print()
x=uniq[0]
uniq[0]=uniq[len(uniq)-1]
uniq[len(uniq)-1]=x
print(uniq)
print(f'Поменянные местами: {uniq[0]} и {uniq[len(uniq)-1]}\n')

print('Список начиная с 3 элемента с шагом 2: ')
for w in range(2,len(uniq),2):
    print(uniq[w])

print()
if len(uniq) % 2 == 0:
    first_half = uniq[:len(uniq)//2]
    second_half = uniq[len(uniq)//2:]
else:
    first_half = uniq[:len(uniq)//2 + 1]
    second_half = uniq[len(uniq)//2 + 1:]
print(f'Первая часть: {first_half}')
print(f'Вторая часть: {second_half}')

print()
print(f'В обратном порядке: {uniq[::-1]} \n')
print(f'Последние 3 элемента: {uniq[-3:]}')