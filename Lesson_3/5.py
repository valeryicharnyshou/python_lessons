def calc_app():
    total = 0
    ex = False
    while not ex:
        number = input('Введите числа через пробел, q для завершения работы программы: ').split()
        res = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'Q':
                ex = True
                break
            else:
                res = res + int(number[el])
        total = total + res
        print(f'Текущая сумма: {total}')
    print(f'Окончательная сумма: {total}')


calc_app()
