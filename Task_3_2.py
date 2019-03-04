# Во втором массиве сохранить индексы четных элементов первого массива.

import random

SIZE = 20
MIN_LIMIS = 0
MAX_LIMIS = 100

array = [random.randint(MIN_LIMIS, MAX_LIMIS) for _ in range (SIZE)]
print(array)
print()

result = []

for count in range(SIZE):
    if array[count] % 2 == 0:
        result.append(count)

print(result)