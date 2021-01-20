def my_func(num1, num2):
    return num1 / num2


number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))
while True:
    if number2 == 0:
        print("Деление на ноль запрещено!")
        number2 = int(input("Введите корректное значение!: "))
    else:
        break


result = my_func(number1, number2)
print("Результат деления первого числа на второе: ", result)
