"""С помощью среза вывести последние 3 элемента списка"""

import random
numbers = [random.randint(-50, 50) for _ in range(10)]

numbers2 = numbers[-3::]
print(numbers)
print(numbers2)