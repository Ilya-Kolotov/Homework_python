# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import random


list = [random.randint(1, 55) for i in range(10)]
d = {}
for i in list:
    d[i] = i
print(list)
print(f'Список неповторяющихся элементов исходной последовательности {sorted(d.values())}')