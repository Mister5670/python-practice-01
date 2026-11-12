tovary = []
obshaya_summa = 0

while True:
    while True:
        name = input('Введите название товара: ').strip()
        if name == '':
            print('Ошибка: название не должно быть пустым!')
        else:
            break

    while True:
        try:
            price = float(input('Введите цену: '))
            if price <= 0:
                print('Ошибка: цена должна быть положительной!')
            else:
                break
        except ValueError:
            print('Ошибка: введите число!')

    while True:
        try:
            count = int(input('Введите количество: '))
            if count <= 0:
                print('Ошибка: количество должно быть положительным!')
            else:
                break
        except ValueError:
            print('Ошибка: введите целое число!')

    summa_tovara = price * count
    tovary.append((name, summa_tovara))
    obshaya_summa += summa_tovara

    while True:
        answer = input('Добавить ещё один товар? (да/нет): ').lower().strip()
        if answer == 'да':
            print()
            break
        elif answer == 'нет':
            break
        else:
            print("Ошибка: пожалуйста, введите 'да' или 'нет'.")
    if answer == 'нет':
        break

print('\n' + '=' * 40)
print('          ЧЕК ПОКУПКИ')
print('=' * 40)

for name, summa in tovary:
    print(f'{name}: {summa:.0f}')

print(f'\nОбщая стоимость: {obshaya_summa:.0f}')

if 5000 <= obshaya_summa < 10000:
    skidka_procent = 5
elif 10000 <= obshaya_summa < 15000:
    skidka_procent = 10
elif obshaya_summa >= 15000:
    skidka_procent = 15
else:
    skidka_procent = 0

if skidka_procent > 0:
    razmer_skidki = obshaya_summa * (skidka_procent / 100)
    itog = obshaya_summa - razmer_skidki
    print(f'Скидка: {skidka_procent}%')
    print(f'Размер скидки: {razmer_skidki:.0f}')
    print(f'Итоговая стоимость: {itog:.0f}')
else:
    print('Скидка: нет')
    print(f'Итоговая стоимость: {obshaya_summa:.0f}')