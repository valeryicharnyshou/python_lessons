from sys import argv

script_name, hours, hour_pay, bonus = argv


def salary_func(h, h_pay, b):
    return (int(h) * int(h_pay)) + int(b)


print("Зарплата сотрудника составит: ", salary_func(hours, hour_pay, bonus))
