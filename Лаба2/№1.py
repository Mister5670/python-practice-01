for i in range(1,10):
    for c in range(1,11):
        print(f'{i} x {c} = {i*c}')
    print()

a=0
for i in range(1,101):
    if i % 2 != 0:
        a+=i
print(a)

n=int(input('Введите число: '))
for i in range(1,n+1):
    if n%i==0:
        print(f'{i} делитель {n}')

x=int(input('Введите число для факториала: '))
c=1
for i in range(1,x+1):
    c*=i
print(f'Факториал числа: {c}')

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
        fib.append(fib[i-1] + fib[i-2])
    print(fib)