try:
    a = float(input("Введите первое число: "))
    op = input("Введите операцию (+, -, *, /, //, %, ^): ")
    b = float(input("Введите второе число: "))
except ValueError:
    print("Ошибка: введите число!\n")
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
print(res)