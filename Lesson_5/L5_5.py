def sum_app():
    with open('5.txt', 'w+') as f:
        number = input('Введите числа через пробел: ')
        f.writelines(number)
        numbers = number.split()
        print(sum(map(int, numbers)))


sum_app()
