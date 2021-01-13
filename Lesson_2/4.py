user_data = input("Введите несколько слов через пробел:")
user_list = user_data.split()
counter = 1
for i in user_list:
    if len(i) > 10:
        print(counter, ":", i[:10])
    else:
        print(counter, ":", i)
    counter += 1
