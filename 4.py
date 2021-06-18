user_number = int(input("Введите целое положительное число: "))
maximal_number = user_number % 10
temp = user_number // 10
while temp > 0:
    if temp % 10 > maximal_number:
        maximal_number = temp % 10
    temp = temp // 10
print(maximal_number)
