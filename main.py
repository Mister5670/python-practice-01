while True:
    try:
        a = float(input("Введите первое число: "))
        op = input("Введите операцию (+, -, *, /, //, %, ^): ")
        b = float(input("Введите второе число: "))
    except ValueError:
        print("Ошибка: введите число!\n")
        continue

    if op == '+':
        res = a + b
    elif op == '-':
        res = a - b
    elif op == '*':
        res = a * b
    elif op == '/':
        if b == 0:
            res = "Ошибка: деление на ноль!"
        else:
            res = a / b
    elif op == '//':
        if b == 0:
            res = "Ошибка: деление на ноль!"
        else:
            res = a // b
    elif op == '%':
        if b == 0:
            res = "Ошибка: деление на ноль!"
        else:
            res = a % b
    elif op == '^':
        res = a ** b
    else:
        res = "Ошибка: неизвестная операция!"

    print("Результат:", res, "\n")

    while True:
        answer = input("Хотите выполнить ещё одну операцию? (да/нет): ").lower().strip()
        if answer == 'да':
            break
        elif answer == 'нет':
            print("Работа программы завершена.")
            exit()
        else:
            print("Ошибка: пожалуйста, введите 'да' или 'нет'.")