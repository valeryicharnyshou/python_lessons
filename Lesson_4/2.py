some_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [el for number, el in enumerate(some_list) if some_list[number] > some_list[number - 1] and number != 0]
print(new_list)
