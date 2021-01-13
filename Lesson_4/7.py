from math import factorial
n = int(input("Введите число для расчета факториала: "))


def fact(number):
    for i in range(1, number + 1):
        yield factorial(i)


for el in fact(n):
    print(el)
