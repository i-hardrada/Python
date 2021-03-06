# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

ROW = 200
COL = 300
MIN_LIMIS = -10
MAX_LIMIS = 100

matrix = [[random.randint(MIN_LIMIS, MAX_LIMIS) for _ in range (COL)] for _ in range(ROW)]


result = None

for j in range(COL):
    spam_col = matrix [0][j]
    for i in range(ROW):
        if matrix[i][j] < spam_col: spam_col = matrix[i][j]
    if result is None or result < spam_col: result = spam_col

print("Первый среди последних: ", result)

# Замечания к домашке в целом)
# Во первых, искренне надеюсь, что избежал досадных мелких ляпов. Не говоря уже о чудовищных и непростительных ошибках.
# После того, как поумничал, было бы особенно досадно)
# Во вторых, признаю, безобразно поздно. Я правда стараюсь. Однако, и меня не перестают радовать. Arbeit macht frei.
# Буду стараться еще лучше, но дай бог мне вписать учебу в рабочий ритм к концу Вашего курса.
# Мне это неприятно, еще раз извините.
# Ну и в третьих, хотелось бы почитать хорошую фундаментальную книгу по теории алгоритмов и вычислимости.
# Желательно написанную программистом, а не математиком. На русском. И на бумаге. Такой я скромный. Посоветуете?
