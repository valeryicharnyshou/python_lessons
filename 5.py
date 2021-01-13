income = int(input("Введите сумму выручки фирмы: "))
costs = int(input("Введите сумму издержек фирмы: "))
if income > costs:
    print("Фирма приносит прибыль!")
    print("Рентабельность составляет: ", round((income / costs * 100), 1), "%")
    quantity_of_workers = int(input("Введите количество сотрудников в фирме: "))
    print("Прибыль в расчете на одного сотрудника: ", ((income - costs) / quantity_of_workers))
elif income == costs:
    print("Фирма находится в безубытке!")
else:
    print("Фирма работает в убыток!")
