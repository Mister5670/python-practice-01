count = 1
for i in range(1, 6):
    count *= i
print("5! =", count)

count = 1
for i in range(1, 16):
    count *= i
print("15! =", count)

n = int(input("Введите n: "))
count = 1
for i in range(1, n + 1):
    count *= i
print(n, "! =", count)

print("Вводите числа (0 для выхода):")
flag = True
while flag:
    x = int(input())
    count = 1
    if x == 0:
        flag = False
        break
    while x != 0:
        count = count * x
        x -= 1
    print(count)