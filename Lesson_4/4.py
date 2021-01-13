some_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = [i for i in some_list if some_list.count(i) < 2]
print("Результат: ", new_list)
