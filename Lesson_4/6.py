from itertools import count
start_number = int(input("Введите начальное число: "))
for i in count(start_number):
    if i == 10:
        break
    else:
        print(i)
