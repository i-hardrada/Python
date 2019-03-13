# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

SIZE = 10
MIN_LIMIS = 0
MAX_LIMIS = 100

array = [1, 0, 0, 2, 3, 3, 3, 2, 2, 2, 2] # вообще подразумевается генерируемый массив, но как иллюстрация этот лучше
# array = [random.randint(MIN_LIMIS, MAX_LIMIS) for _ in range (SIZE)]
print(array)


fat = [MIN_LIMIS - 1, 0]        # массив выбран для удобства отладки
flat = [MAX_LIMIS + 1, 0]

for count in range(SIZE):
    if array[count] > fat[0]: fat = [array[count], count]
    elif array[count] == fat[0]: fat.append(count)
    if array[count] < flat[0]: flat = [array[count], count]
    elif array[count] == flat[0]: flat.append(count)

#    print("Шаг", count + 1)
#    print(fat)
#    print(flat)
#    print()

for count in range(min(len(fat) - 1, len(flat) - 1)):
    array[fat[count + 1]], array[flat[count + 1]] = array[flat[count + 1]], array[fat[count + 1]]

print(array)

# Строго говоря, задача поставлена некорректно. Из текста следует, что минимальных и максимальных элементов ожидается
# по одному, что для случайного массива совсем не обязательно . И даже если найти и попытаться переставить их все,
# неопределенность сохраняется в случае неравного их количества.
# Методисту звездочку и сто грамм за сбитый.