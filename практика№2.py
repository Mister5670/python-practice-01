while True:
    print('1. Градус Цельсия -> Градус Фаренгейта')
    print('2. Километры -> Мили')
    print('3. Килограммы -> Фунты')
    print('4. Метры -> Футы')
    print('5. Литры -> Галлоны')
    print('6. Мегабайты -> Гигабайты')
    print('Выберите один из типов преобразования:')
    a=input()
    if a=='1':
        try:
            print('Введите температуру:')
            x=float(input())
            y=(x*1.8)+32
            print(f'{x} С = {y} F')
        except ValueError:
            print('Ошибка, введите число')
    elif a=='2':
        try:
            print('Введите километры:')
            x=float(input())
            y=x*1.6
            print(f'{x} Км = {y} Миль')
        except ValueError:
            print('Ошибка, введите число')
    elif a=='3':
        try:
            print('Введите Килограммы:')
            x=float(input())
            y=x*2.2
            print(f'{x} Кг = {y} Фунтов')
        except ValueError:
            print('Ошибка, введите число')
    elif a=='4':
        try:
            print('Введите метры:')
            x=float(input())
            y=x*3.28
            print(f'{x} М = {y} футов')
        except ValueError:
            print('Ошибка, введите число')
    elif a=='5':
        try:
            print('Введите литры:')
            x=float(input())
            y=x/3.79
            print(f'{x} Л = {y} Галлонов')
        except ValueError:
            print('Ошибка, введите число')
    elif a=='6':
        try:
            print('Введите мегабайты:')
            x=float(input())
            y=x/1024
            print(f'{x} Мб = {y} Гб')
        except ValueError:
            print('Ошибка, введите число')
    else:
        print('Неизвестный тип преобразования')
    while True:
        a=input('Выполнить ещё одно преобразование? (да/нет): ').lower().strip()
        if a=='да':
            break
        elif a=='нет':
            print('Работа программы завершена')
            exit()
        else:
            print("Ошибка: пожалуйста, введите 'да' или 'нет'.")