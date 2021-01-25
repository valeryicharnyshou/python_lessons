number_of_month = int(input("Введите месяц в виде целого числа от 1 до 12:"))
winter = dict(January=1, February=2, December=12)
spring = dict(March=3, April=4, May=5)
summer = dict(June=6, July=7, August=8)
autumn = dict(September=9, October=10, November=11)
if number_of_month in winter.values():
    print("Это месяц зимы!")
elif number_of_month in spring.values():
    print("Это месяц весны!")
elif number_of_month in summer.values():
    print("Это месяц лета!")
else:
    print("Это месяц осени!")
