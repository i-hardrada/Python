# Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 50
MIN_LIMIS = 0
MAX_LIMIS = 10

array = [random.randint(MIN_LIMIS, MAX_LIMIS) for _ in range(SIZE)]
print(array)
print()

# s = 0
for _ in range(SIZE):
    flag = 0
    for count in range(SIZE - 1):
        if array[count] > array[count + 1]:
            array[count], array[count + 1] = array[count + 1], array[count]
            flag = 1
#       s += 1
    if flag == 0: break
print(array)
# print("Итераций сортировки:", s)
print()

#       ^        ^         ^
#       |        |         |
# Пожалуй, решение на грани фола) Но уж больно мне понравилась идея анализа упорядоченного массива.
# Быстро, дешего и сердито.

freq = 1
shadow_freq = 0
array.append(None)
result = [array[0], freq]

for count in range(SIZE):
    if array[count] == array[count + 1]:
        freq += 1
    else:
        if freq >= shadow_freq:
            shadow_freq = freq
            result = [array[count], freq]
        freq = 1

print("Число", result[0], "встречается", result[1], "раз(а)")

# !!!
# [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] - думаю пойдет, если число одно, можно утверждать, что оно то чаще всего и встречается
# [1, 1, 1, 1, 2, 2, 3, 3, 3, 3] - уже нет. Снова неопределенность.
# Тут канешна мооожно написать правильную программу) А можно прочитать "чаще всего" как "не реже остальных".
# И выразить лицом Дзен.
# Пожалуй, еще звездочку методисту.