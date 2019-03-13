# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив,
# элементы которого это цифры числа.

from collections import deque

CUTTER = 4

HEX_DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
DEC_NUMBERS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

Hex = dict(zip(HEX_DIGITS, DEC_NUMBERS))
Dec = dict(zip(DEC_NUMBERS, HEX_DIGITS))

a = input("Введите число a (0-f): ")
b = input("Введите число b (0-f): ")
print()

hex_array_a = list(a)
hex_array_b = list(b)
hex_array_a.reverse()
hex_array_b.reverse()

hex_array_a.extend('0' * (len(b) - len(a)))
hex_array_b.extend('0' * (len(a) - len(b)))


add_result = deque([])

up = 0
for i in range(len(hex_array_a)):
    spam = Hex.get(hex_array_a[i]) + Hex.get(hex_array_b[i]) + up
    up = spam >> CUTTER
    add_result.appendleft(spam - (up << CUTTER))
if up != 0: add_result.appendleft(up)

for count in range(len(add_result)): add_result[count] = Dec.get(add_result[count])


mul_result = deque([])

for i in range(len(b)):
    up = 0
    buf = deque([])
    for j in range(len(a)):
        spam = Hex.get(hex_array_a[j]) * Hex.get(hex_array_b[i]) + up
        up = spam >> CUTTER
        buf.append(spam - (up << CUTTER))
    if up != 0: buf.append(up)
    for _ in range(i): buf.appendleft(0)
    mul_result.extend(0 for _ in range(len(buf)-len(mul_result)))

    up = 0
    for count in range(len(buf)):
        spam = mul_result[count] + buf[count] + up
        up = spam >> CUTTER
        mul_result[count] = spam - (up << CUTTER)
    if up != 0: mul_result.append(up)
# Наверное стоило вынести суммирование в функцию. Код был бы почище, можно было бы не использовать
# десятичное представление, выкинуть лишний словарь... Ну да ладна.

mul_result.reverse()
for count in range(len(mul_result)): mul_result[count] = Dec.get(mul_result[count])


print('a + b = ', list(add_result))
print()
print('a * b = ', list(mul_result))

# Если это то, чем программисты каждый день занимаются на работе...
# Боже, какое счастье, что я не программист.