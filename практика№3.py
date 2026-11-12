while True:
    try:
        print('Введите число: ')
        a=int(input())
    except ValueError:
        print('Ошибка, введите число')
        continue
    print(f'Ваше число {a}')
    if a<0:
        res='нет'
        print(f'положительное: {res}')
    elif a>0:
        res='да'
        print(f'положительное: {res}')
    else:
        res='0'
        print(f'число: {res}')
    if a%2==0:
        res='да'
        print(f'четное: {res}')
    else:
        res='нет'
        print(f'четное: {res}')
    if a%3==0:
        res='да'
        print(f'делится без остатка на 3: {res}')
    else:
        res='нет'
        print(f'делится без остатка на 3: {res}')
    if a%5==0:
        res = 'да'
        print(f'делится без остатка на 5: {res}')
    else:
        res = 'нет'
        print(f'делится без остатка на 5: {res}')
    import math
    if a >= 0 and math.isqrt(a) ** 2 == a:
        res = 'да'
        print(f'Полный квадрат: {res}')
    else:
        res = 'нет'
        print(f'Полный квадрат: {res}')
    if a < 2:
        res = 'нет'
    else:
        res = 'да'
        for i in range(2, int(abs(a) ** 0.5) + 1):
            if a % i == 0:
                res = 'нет'
                break
    print(f'простое: {res}')
    print(f'Количество цифр {len(str(abs(a)))}')
    while True:
        a=input('Проверить ещё одно число? (да/нет):').lower().strip()
        if a=='да':
            break
        elif a=='нет':
            print('работа программы завершена')
            exit()
        else:
            print("Ошибка: пожалуйста, введите 'да' или 'нет'.")