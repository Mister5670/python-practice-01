c = 0
for y in range(1,11):
    c += y
print('сумма от 1 до 10: ', c)
n = int(input())
c1 = 0
c2 = 0
for a in range(1,n+1):
    c1 += a
    if a % 2 == 0:
        c2 += a
print(c1)
print(c2)