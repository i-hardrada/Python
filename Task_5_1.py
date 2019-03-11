# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа)
# для каждого предприятия.. Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести
# наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль
# ниже среднего.

from collections import namedtuple

num = int(input('Введите число предприятий: '))

array = []
hoarder = 0
Company = namedtuple('Company', 'brand, q1, q2, q3, q4, total')

for count in range(num):
    brand = input('Введите наименование предприятия ' + str(count+1) + ': ')
    q1 = int(input('Прибыль в первом квартале:    '))
    q2 = int(input('Прибыль во втором квартале:   '))
    q3 = int(input('Прибыль в третьем квартале:   '))
    q4 = int(input('Прибыль в четвертом квартале: '))
    total = q1 + q2 + q3 + q4
    hoarder += total
    array.append(Company(brand, q1, q2, q3, q4, total))
    print()

total_av = hoarder / num

print('Предприятия с прибылью выше средней: ')
for count in range(num):
    if array[count].total > total_av: print(array[count].brand)
print()

print('Предприятия с прибылью ниже средней: ')
for count in range(num):
    if array[count].total < total_av: print(array[count].brand)
print()

# Да, я уже посмотрел разбор) Пусть остается как было. Fair play.