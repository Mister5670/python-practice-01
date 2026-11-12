x = int(input())
if 10 <= x <= 99:
    x = str(x)
    summa = int(x[0]) + int(x[1])
    proizv = int(x[0]) * int(x[1])
    print("сумма цифр:", summa)
    print("произведение цифр:", proizv)
elif 100 <= x <= 999:
    x = str(x)
    summa = int(x[0]) + int(x[1]) + int(x[2])
    first_last = x[0], x[2]
    print("сумма цифр:", summa)
    print("первая и последняя цифры:",first_last[0],first_last[1])
else:
    print("число должно быть двузначным или трёхзначным")
