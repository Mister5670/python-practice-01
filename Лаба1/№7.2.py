flag = True
while flag:
    x = int(input())
    count = 1
    if x == 0 :
        flag = False
        break
    while x != 0:
        count = count * x
        x -= 1
    print(count)