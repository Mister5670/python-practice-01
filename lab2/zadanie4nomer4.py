"""Проверить, является ли одно множество подмножеством другого"""

mnozhestvo1 = {1,2,3,4,5,6,7,8,9,10}
mnozhestvo2 = {2,4,6,8,10}

if mnozhestvo1 == mnozhestvo2:
    print("Множества одинаковые")
elif mnozhestvo1 > mnozhestvo2:
    print("Множество 2 является подмножеством множества 1")
elif mnozhestvo1 < mnozhestvo2:
    print("Множество 1 является подмножеством множества 2")
else:
    print("Множества не пересекаются")