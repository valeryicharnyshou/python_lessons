n = input("Введите целое положительное число: ")
if int(n) <= 0:
    while int(n) <= 0:
        n = input("Введено неверное число! Повторите ввод!: ")
    print("Сумма чисел равна: :", int(n) + int(n + n) + int(n + n + n))
else:
    print("Сумма чисел равна: :", int(n) + int(n + n) + int(n + n + n))
