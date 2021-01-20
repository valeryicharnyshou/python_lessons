number_of_month = int(input("Введите месяц в виде целого числа от 1 до 12:"))
winter = [1, 2, 12]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]
if number_of_month in winter:
    print("Это месяц зимы!")
elif number_of_month in spring:
    print("Это месяц весны!")
elif number_of_month in summer:
    print("Это месяц лета!")
else:
    print("Это месяц осени!")
