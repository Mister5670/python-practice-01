sum1 = 0
while True:
    x = int(input())
    if x == 0:
        break
    sum1 += x
print(sum1)

count = 0
while True:
    x = int(input())
    if x < 0:
        break
    count += 1
print(count)

sum3 = 0
while True:
    x = int(input())
    if x % 2 == 0:
        break
    sum3 += x
print(sum3)

sum4 = 0
count4 = 0
while True:
    x = int(input())
    if x > 100:
        break
    sum4 += x
    count4 += 1
if count4 > 0:
    print(sum4 / count4)
else:
    print(0)