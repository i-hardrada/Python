# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.


for denominator in range(2, 10):
    spam = 0
    count = 0
    while True:
        spam = count * denominator
        if spam > 99:
            count -= 1
            break
        count += 1
    print ("Кратных", denominator, "-", count)


