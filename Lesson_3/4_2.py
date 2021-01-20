def my_func(x, y):
    counter = 1
    temp_result = 1 / x
    while counter < abs(y):
        temp_result = (1 / x) * temp_result
        counter += 1
    return temp_result


number1 = float(input("Введите действительное положительное число: "))
while number1 < 0:
    number1 = float(input("Необходимо ввести ПОЛОЖИТЕЛЬНОЕ действительное число! "))
number2 = int(input("Введите целое отрицательное число: "))
while number2 > 0:
    number2 = int(input("Необходимо ввести ОТРИЦАТЕЛЬНОЕ целое число! "))
print(my_func(number1, number2))
